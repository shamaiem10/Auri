<div align="center">

# 🎧🎤 AURI
### *Talk, Listen & Chat with Your AI Assistant*

A real-time **AI Voice Chatbot** built with Flask, Groq LLM, AssemblyAI, and gTTS — with memory, speech-to-text, text-to-speech, and a WhatsApp-style pink, yellow & black chat interface.

<br/>

![Python](https://img.shields.io/badge/Python-3.11+-FF2E93?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask&logoColor=FFD93D)
![AssemblyAI](https://img.shields.io/badge/AssemblyAI-STT-FF2E93?style=for-the-badge&logo=assemblyai&logoColor=white)
![Groq LLM](https://img.shields.io/badge/Groq-LLM-000000?style=for-the-badge&logo=groq&logoColor=FFD93D)
![gTTS](https://img.shields.io/badge/gTTS-TTS-FFD93D?style=for-the-badge&logo=googlecloud&logoColor=000000)

🎀 ─────────────────────────────────────────── 🎀

</div>

## 📸 Screenshot

<div align="center">

![AI Voice Chatbot](https://github.com/shamaiem10/Auri/blob/main/static/Screenshot%202025-09-28%20015851.png)

*Real-time AI Voice Chatbot interface with horizontal chat layout.*

</div>

<br/>

## 🚀 Features

<div align="center">

| | |
|:---:|:---|
| 🎙️ **Real-Time Voice Chat** | Speak to the bot — it transcribes your audio instantly |
| 🔊 **Text-to-Speech** | Bot responses are converted to speech using gTTS |
| 🧠 **Memory of Last 5 Interactions** | Keeps context of previous conversations |
| 💗 **Horizontal Chat UI** | Pink, light yellow, black theme with Bootstrap icons |
| 💬 **WhatsApp-Style Bubbles** | Alternating left (bot) and right (user) messages |
| ▶️ **Audio Playback** | Play bot responses directly in the browser |
| 🧩 **Lightweight & Extensible** | Easily modify or integrate with other AI models |

</div>

---

## 🛠️ Tech Stack

### ⚙️ Backend

<div align="center">

| Technology | Purpose |
|:---:|---|
| Python 3.11+ | Core backend logic |
| Flask | Web framework for routing, serving templates, and APIs |
| AssemblyAI | Speech-to-Text (transcription of user audio) |
| Groq LLM | Large Language Model for generating bot responses |
| gTTS | Convert bot responses to audio |
| dotenv | Load environment variables securely |
| requests | HTTP requests for AssemblyAI and Groq APIs |

</div>

### 🎨 Frontend

<div align="center">

| Technology | Purpose |
|:---:|---|
| HTML5 & CSS3 | Core UI structure and styling |
| JavaScript | Microphone recording, audio playback, dynamic chat updates |
| Bootstrap Icons | Modern icons for mic, stop buttons, and UI elements |
| Responsive Horizontal Layout | Chat on left, controls + audio on right |

</div>

### 🧰 Others

<div align="center">

| Tool | Purpose |
|:---:|---|
| tempfile / static/audio folder | Store temporary user and bot audio files |
| OS module | Handle file paths and directories |
| time module | Generate unique filenames and poll for transcription status |

</div>

---

## 💾 Project Structure

```bash
flask_voice_bot/
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Frontend HTML
└── static/
    ├── audio/               # Folder to store user & bot audio
    ├── style.css             # Chat UI styling
    └── script.js              # Frontend JS for recording & chat logic
```

---

## ⚡ Features In Detail

**Real-Time STT + LLM Response**
- Records voice via the WebRTC / MediaRecorder API
- Sends audio to AssemblyAI for transcription
- Sends the last 5 conversation turns to Groq LLM as context
- Converts the response to speech via gTTS

**Memory Management**
- Stores the last 5 user–bot pairs in a Python list
- Ensures coherent conversation context
- Automatically trims old messages to avoid memory overload

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/shamaiem10/Auri.git
cd Auri
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set environment variables**

Create a `.env` file with:
```bash
ASSEMBLYAI_API_KEY=your_assemblyai_key
GROQ_API_KEY=your_groq_api_key
```

**5. Run the Flask app**
```bash
python app.py
```

**6. Access the chatbot**

Open your browser at `http://127.0.0.1:5000/`.

---

## 📌 How It Works

<div align="center">

| Step | Action |
|:---:|---|
| 1️⃣ | User clicks record → records voice → sends to Flask backend |
| 2️⃣ | Flask uploads audio to AssemblyAI, gets transcription text |
| 3️⃣ | Last 5 conversation memory + user text sent to Groq LLM |
| 4️⃣ | LLM returns bot text → converted to speech (gTTS) → sent to frontend |
| 5️⃣ | Frontend updates chat bubbles dynamically and plays bot audio |

</div>

---

<div align="center">

🎀 ─────────────────────────────────────────── 🎀

**Happy coding and enjoy chatting with your AI Voice Bot!** 🎤🤖

</div>
