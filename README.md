# 💬 LLaMA Conversational Chatbot (Groq API) with Voice Input

This is a conversational chatbot built with **Streamlit** and **Groq API (LLaMA model)** that supports **both text and voice input**. The bot remembers your chat history, replies to your questions, and plays audio of its responses using **text-to-speech (gTTS)**.

---

## 🚀 Features

- Chat with LLaMA in real-time.
- Supports both **text** and **voice** input.
- Remembers your conversation history.
- Text-to-speech (TTS) audio playback of responses.
- "Clear Chat" button to reset the conversation.
- Clean and mobile-friendly chat interface.

---

## 🛠️ Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/bhoomi1301/Llama_chatbot.git
cd Llama_chatbot
```

2️⃣ **Set up a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

_Example `requirements.txt`:_

```
streamlit
requests
python-dotenv
gTTS
speechrecognition
pyaudio
openai  # Or the Groq client library you are using
```

**Note:**  
- On some systems, you may need to install `PyAudio` with:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 Set up API Keys

Make sure you have your **Groq API key** or **OpenAI-compatible API key** set up.

Example (for terminal use):

```bash
export OPENAI_API_KEY=your_api_key_here
```

Or configure it in your `chatbot.py`.

---

## ▶️ How to Run

```bash
streamlit run app.py
```

---

## 🧠 Project Structure

```
llama-chatbot/
├── app.py
├── chatbot.py
├── requirements.txt
└── README.md
```

- **app.py:** Main Streamlit app.
- **chatbot.py:** Handles communication with the LLaMA (Groq API).

---

## 📝 Example `chatbot.py`

Example code to interact with the API:

```python
import openai  # Or the Groq API client if using Groq

def chat_with_llama(chat_history):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace with your Groq-compatible model name
        messages=chat_history
    )
    return response['choices'][0]['message']['content']
```

---

## 🎤 Voice Input

- The app uses **SpeechRecognition** and **PyAudio** to capture voice.
- Simply tap the **"Speak"** button to record your voice (up to 30 seconds).
- The bot converts your voice to text, replies, and reads the reply aloud.

---

## 📱 Mobile-Friendly UX

✅ Works well on mobile devices.  
✅ Easy toggle between **Type** and **Speak** modes.  
✅ One-tap "Clear Chat" button to reset the conversation.

---

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [Groq API / OpenAI API](https://groq.com/)

---

## 🔗 Connect with Me

[LinkedIn - Bhoomika N S](https://www.linkedin.com/in/bhoomikans)
