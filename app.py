import os
import time
import requests
from flask import Flask, render_template, request, jsonify, send_from_directory
from gtts import gTTS
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/audio"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Keep last 5 messages for memory
conversation_memory = []  # list of {"role": "user"/"bot", "content": text}

# --- Transcription function ---
def transcribe_assembly(file_path):
    headers = {"authorization": ASSEMBLYAI_API_KEY}
    upload_url = "https://api.assemblyai.com/v2/upload"

    def read_file_in_chunks(f, chunk_size=5242880):
        while True:
            data = f.read(chunk_size)
            if not data: break
            yield data

    with open(file_path, "rb") as f:
        response = requests.post(upload_url, headers=headers, data=read_file_in_chunks(f))
    audio_url = response.json()["upload_url"]

    transcript_request = {"audio_url": audio_url}
    response = requests.post("https://api.assemblyai.com/v2/transcript", json=transcript_request, headers=headers)
    transcript_id = response.json()["id"]

    import time
    while True:
        res = requests.get(f"https://api.assemblyai.com/v2/transcript/{transcript_id}", headers=headers).json()
        if res["status"] == "completed":
            return res["text"]
        elif res["status"] == "error":
            raise Exception(res["error"])
        time.sleep(2)

# --- Main page ---
@app.route("/")
def index():
    return render_template("index.html")

# --- Audio processing ---
@app.route("/process_audio", methods=["POST"])
def process_audio():
    global conversation_memory

    audio_file = request.files.get("audio_file")
    if not audio_file:
        return jsonify({"error": "No audio file provided"}), 400

    filename = f"user_audio_{int(time.time())}.wav"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    audio_file.save(file_path)

    # Transcribe
    user_text = transcribe_assembly(file_path)

    # Add user message to memory
    conversation_memory.append({"role": "user", "content": user_text})
    if len(conversation_memory) > 10:  # keep max 10 items to maintain last 5 user+bot pairs
        conversation_memory = conversation_memory[-10:]

    # Prepare memory messages for Groq
    memory_messages = conversation_memory[-10:]  # last 5 interactions
    groq_response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=memory_messages
    )
    bot_text = groq_response.choices[0].message.content

    # Add bot message to memory
    conversation_memory.append({"role": "bot", "content": bot_text})
    if len(conversation_memory) > 10:
        conversation_memory = conversation_memory[-10:]

    # Convert bot text to speech
    tts = gTTS(bot_text)
    audio_filename = f"bot_response_{int(time.time())}.mp3"
    audio_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_filename)
    tts.save(audio_path)

    return jsonify({
        "user_text": user_text,
        "bot_text": bot_text,
        "audio_url": f"/audio/{audio_filename}"
    })

# --- Serve audio files ---
@app.route("/audio/<filename>")
def get_audio(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
