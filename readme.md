# 🤖 Jarvis Voice Assistant (Python)

A powerful voice-controlled assistant built using Python that can perform tasks like opening websites, playing music, fetching news, and responding with speech — inspired by Iron Man’s JARVIS.

---

## 🚀 Features

* 🎤 Voice Recognition using Google Speech API
* 🔊 Text-to-Speech response system
* 🌐 Open popular websites via voice commands
* 🎵 Play songs directly on YouTube
* 📰 Fetch latest news headlines (India)
* ⏰ Tell current time and date
* 🧠 Smart command handling using dictionaries
* ❌ Error handling for better reliability

---

## 🛠️ Tech Stack

* Python 3
* speech_recognition
* pyttsx3
* requests
* webbrowser
* python-dotenv

---

## 📂 Project Structure

```
Jarvis/
│── main.py
│── README.md
│── requirements.txt
│── .gitignore
│── .env.example   # Example API key format
│── .env           # Not pushed to GitHub
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ⚠️ Fix PyAudio (Windows Users)

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 API Key Setup

This project uses **NewsAPI** to fetch headlines.

⚠️ The API key is **not included** in this repository (for security reasons or it may have expired).

### 👉 Steps to add your API key:

1. Go to https://newsapi.org
2. Sign up and generate your API key
3. Create a `.env` file in the root directory
4. Add your key:

```bash
API_KEY=your_api_key_here
```

5. Save and run the project

---

💡 If your API key stops working, simply generate a new one and update the `.env` file.

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🎯 Usage

1. Say **"Jarvis"** to activate
2. Then give commands like:

### 🌐 Open Websites

* "open google"
* "open youtube"
* "open linkedin"
* "open whatsapp"

### 🎵 Play Songs

* "play sunday"
* "play dj"
* "play animal"

### 🧠 Utility Commands

* "what is the time"
* "what is the date"
* "news"
* "exit"

---

## 🧠 How It Works

* Converts speech → text using SpeechRecognition
* Processes commands using keyword matching
* Executes actions like opening websites, playing music, and fetching news
* Responds using text-to-speech

---

## ⚠️ Important Notes

* Requires internet connection
* Ensure microphone access is enabled
* Do NOT upload your `.env` file
* Add `.env` to `.gitignore`

---

## 🚀 Future Improvements

* 🤖 ChatGPT integration for smarter conversations
* 🖥️ GUI interface (Tkinter / PyQt)
* 🔊 Wake word detection (always listening mode)
* 📧 Automation tasks (emails, reminders, etc.)
* 🌍 Multi-language support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request 🚀

---

## 👨‍💻 Author

**Ayush Kumar**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---

## 📜 License

This project is open-source and available under the MIT License.
