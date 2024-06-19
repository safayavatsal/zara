import pyttsx3
from datetime import date
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#0 for male voice
#1 for female voice
engine.setProperty('voice',voices[0].id)


def speak(audio):
    print(".......")
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<= 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi I am Cutie..How may i help you?")
def telldate():
    d=str(date.today())
    print(d)
    speak("Today's date is "+d)
def telltime():
    t=str(datetime.datetime.now().strftime("%H:%M:%S"))
    print(t)
    speak("Time is "+t)
def givecommand():
    a=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        a.pause_threshold=0.5    
        audio=a.listen(source)
    try:
        print("Recognizing.....")
        query=a.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Unable to get you.Please say it again")
        return "None"
    return query


if __name__=="__main__":
    wishme()
    while True:
        query=givecommand().lower()

        if 'wikipedia' in query:
            try:
                speak('Searching in wikipedia')
                query=query.replace('wikipedia',"")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except:
                speak("Unable to catch you")
        elif "time" in query:
            telltime()
        elif "date" in query:
            telldate()
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open kaggle" in query:
            webbrowser.open("kaggle.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open codeforces" in query:
            webbrowser.open("codeforces.com")
        elif "open leetcode" in query:
            webbrowser.open("leetcode.com")
        elif "open chat GPT" in query:
            webbrowser.open("chat.openai.com")
        
        elif "open coding ninjas" in query:
            webbrowser.open(r"https://www.codingninjas.com/")
        elif "play music" in query:
            music_dir=r"Music"
            songs=os.listdir(music_dir)
            print(songs)
            n=random.randint(0,11)
            os.startfile(os.path.join(music_dir,songs[n]))
        
        elif "open translator" in query:
            webbrowser.open("translate.google.com")
        elif "open word" in query:
            webbrowser.open(r"WINWORD.EXE")
        elif "open powerpoint" in query:
            webbrowser.open(r"POWERPNT.EXE")
        elif "open excel" in query:
            webbrowser.open(r"EXCEL.EXE")
        elif "hobbies" in query:
            s=["dancing","singing","drawing","listening music"]
            speak(s)
        elif "thank" in query:
            speak("My Pleasure")
        
        elif "your name" in query:
            speak("I am Zira.A speech virtual assistant created by Niharika Varshney")
        elif "cutie quit" in query:
            speak("Hope you had a great day")
            quit()


