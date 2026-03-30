import speech_recognition as sr
import webbrowser
import requests
import pyttsx3
import datetime
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Websites dictionary
sites = {
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "linkedin": "https://linkedin.com",
    "youtube": "https://youtube.com",
    "whatsapp": "https://web.whatsapp.com"
}

# Songs dictionary
songs = {
    "sunday": "https://youtu.be/lpyQhpksHRI",
    "murder": "https://youtu.be/uSibwB2TQC4",
    "dj": "https://youtu.be/DYO_GLIWlRA",
    "zara sa": "https://youtu.be/5IY4BNj0-10",
    "animal": "https://youtu.be/iAIBF2ngbWY",
    "brown": "https://youtu.be/eizmCZv3aKI",
    "stealth": "https://youtu.be/JjPFHwa_12g",
    "million": "https://youtu.be/XO8wew38VM8",
    "dope": "https://youtu.be/NrXdauEv9HY",
    "bonita": "https://youtu.be/q3EsYvIapPQ"
}

def get_news():
    if not API_KEY:
        speak("API key not found")
        return

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    try:
        r = requests.get(url)
        data = r.json()

        speak("Here are the top headlines")
        for article in data["articles"][:5]:
            speak(article["title"])
    except:
        speak("Unable to fetch news")

def process_command(command):
    command = command.lower()

    # Open websites
    for site in sites:
        if f"open {site}" in command:
            speak(f"Opening {site}")
            webbrowser.open(sites[site])
            return

    # Play songs
    if "play" in command:
        for song in songs:
            if song in command:
                speak(f"Playing {song}")
                webbrowser.open(songs[song])
                return

    # Time
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    # Date
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date}")

    # News
    elif "news" in command:
        get_news()

    # Exit
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that")

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        return recognizer.recognize_google(audio)
    except:
        return ""

# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis")
    speak("Say Jarvis to activate")

    while True:
        word = listen()

        if "jarvis" in word.lower():
            speak("Yes, how can I help you?")
            command = listen()
            if command:
                print("Command:", command)
                process_command(command)