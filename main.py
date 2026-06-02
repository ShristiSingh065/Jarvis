import win32com.client
import webbrowser
import time
import musiclib
import speech_recognition as sr
from dotenv import load_dotenv
import os
load_dotenv()

newsapi = os.getenv("NEWS_API_KEY")
recognizer=sr.Recognizer()
import requests
speaker = win32com.client.Dispatch("SAPI.SpVoice")

newsapi = os.getenv("NEWS_API_KEY")

def speak(text):
    speaker.Speak(text)
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]
        link=musiclib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={newsapi}"
)
        if r.status_code==200:
            data=r.json()
            articles=data.get("articles",[])
            for article in articles:
                speak(article['title'])
if __name__ == "__main__":
    speak("Initializing..")
    while True:
        r=sr.Recognizer()
        
        print ("recognizing..")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=3)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                 print("Jarvis detected")
                 speak("ya")
                 time.sleep(2)
                 with sr.Microphone() as source:
                    print("Jarvis active")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    print("Command heard:", command)
                    processcommand(command)
        except Exception as e:
            print("ERROR:", e)
