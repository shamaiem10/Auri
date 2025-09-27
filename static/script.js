let mediaRecorder;
let audioChunks = [];
const chatBox = document.getElementById('chatBox');

const recordBtn = document.getElementById('recordBtn');
const stopBtn = document.getElementById('stopBtn');
const botAudioEl = document.getElementById('botAudio');

recordBtn.onclick = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    audioChunks = [];

    mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

    mediaRecorder.onstop = async () => {
        const blob = new Blob(audioChunks, { type: 'audio/wav' });
        const formData = new FormData();
        formData.append('audio_file', blob, 'user_audio.wav');

        addMessage('You', 'Recording sent...', 'user');

        const res = await fetch('/process_audio', { method: 'POST', body: formData });
        const data = await res.json();

        addMessage('You', data.user_text, 'user');
        addMessage('Bot', data.bot_text, 'bot');

        // Play bot audio
        botAudioEl.src = data.audio_url;
        botAudioEl.play();
    };

    mediaRecorder.start();
    recordBtn.disabled = true;
    stopBtn.disabled = false;
};

stopBtn.onclick = () => {
    mediaRecorder.stop();
    recordBtn.disabled = false;
    stopBtn.disabled = true;
};

function addMessage(sender, text, type) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message');
    msgDiv.classList.add(type === 'user' ? 'user-msg' : 'bot-msg');
    msgDiv.textContent = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
