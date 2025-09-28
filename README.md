# 🎧🎤 AURI – Talk, Listen & Chat with Your AI Assistant

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-2.3-green?style=flat-square)
![AssemblyAI](https://img.shields.io/badge/AssemblyAI-STT-orange?style=flat-square)
![Groq LLM](https://img.shields.io/badge/Groq-LLM-purple?style=flat-square)
![gTTS](https://img.shields.io/badge/gTTS-TTS-red?style=flat-square)

A modern **real-time AI Voice Chatbot** built with **Flask, Groq LLM, AssemblyAI, and gTTS**, featuring:  

- Memory of last 5 interactions  
- Speech-to-text  
- Text-to-speech  
- A **beautiful responsive chat interface** with pink, yellow, and black theme  

The UI mimics a modern chat app, inspired by **WhatsApp-style chat bubbles** with a horizontal layout.

---
## 📸 Screenshot

![AI Voice Chatbot](https://github.com/shamaiem10/Auri/blob/main/static/Screenshot%202025-09-28%20015851.png)
*Real-time AI Voice Chatbot interface with horizontal chat layout.*


## 🚀 Features

- **Real-Time Voice Chat** – Speak to the bot, it transcribes your audio instantly.  
- **Text-to-Speech** – Bot responses are converted to speech using gTTS.  
- **Memory of Last 5 Interactions** – Keeps context of previous conversations.  
- **Beautiful Horizontal Chat UI** – Pink, light yellow, black theme with Bootstrap icons.  
- **WhatsApp-Style Chat Bubbles** – Alternating left (bot) and right (user) messages.  
- **Audio Playback** – Play bot responses directly in the browser.  
- **Lightweight & Extensible** – Easily modify or integrate with other AI models.  

---

## 🛠️ Tech Stack

### Backend

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Core backend logic |
| Flask | Web framework for routing, serving templates, and APIs |
| AssemblyAI | Speech-to-Text (transcription of user audio) |
| Groq LLM | Large Language Model for generating bot responses |
| gTTS | Convert bot responses to audio |
| dotenv | Load environment variables securely |
| requests | HTTP requests for AssemblyAI and Groq APIs |

### Frontend

| Technology | Purpose |
|------------|---------|
| HTML5 & CSS3 | Core UI structure and styling |
| JavaScript | Microphone recording, audio playback, dynamic chat updates |
| Bootstrap Icons | Modern icons for mic, stop buttons, and UI elements |
| Responsive Horizontal Layout | Chat on left, controls + audio on right |

### Others

| Tool | Purpose |
|------|---------|
| tempfile / static/audio folder | Store temporary user and bot audio files |
| OS module | Handle file paths and directories |
| time module | Generate unique filenames and poll for transcription status |

---
## 💾 Project Structure
```bash
flask_voice_bot/
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Frontend HTML
└── static/
    ├── audio/               # Folder to store user & bot audio
    ├── style.css            # Chat UI styling
    └── script.js            # Frontend JS for recording & chat logic
```

## ⚡ Features In Detail

- Real-Time STT + LLM Response

- Records voice via WebRTC / MediaRecorder API.

- Sends audio to AssemblyAI for transcription.

- Memory of last 5 conversations sent to Groq LLM.

- Response converted to speech via gTTS.

- Memory Management

- Stores the last 5 user-bot pairs in Python list.

- Ensures coherent conversation context.

- Automatically trims old messages to avoid memory overload.


## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/shamaiem10/Auri.git
cd Auri
```



2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set environment variables
Create a .env file with:

```bash
ASSEMBLYAI_API_KEY=your_assemblyai_key
GROQ_API_KEY=your_groq_api_key
```

5. Run the Flask app
```bash
python app.py
```

6. Access the chatbot
```bash
Open your browser at http://127.0.0.1:5000/.
```


## 📌 How It Works

1. User clicks record → records voice → sends to Flask backend.

2. Flask uploads audio to AssemblyAI, gets transcription text.

3. Last 5 conversation memory + user text sent to Groq LLM.

4. LLM returns bot text → converted to speech (gTTS) → sent to frontend.

5. Frontend updates chat bubbles dynamically and plays bot audio.

> Happy coding and enjoy chatting with your AI Voice Bot! 🎤🤖



