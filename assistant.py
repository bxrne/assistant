import speech_recognition as sr 
import webbrowser
import time
import os
from news import *

r = sr.Recognizer()

def speak(y):
    os.system("espeak -s 170 '{}'".format(y))

def listen(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            speak("Excuse me")
        except sr.RequestError:
            speak("Service is down")
        return voice_data

def respond(voice_data):
    if 'good morning' in voice_data:
        speak("Good morning, what do you need?")
    if 'search' in voice_data:
        search = listen('Search for what')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
    if 'goodbye' in voice_data:
        speak("Goodbye")
        exit()
    if 'joke' in voice_data:
        speak("Wherever I go  - there I am")
    if 'news' in voice_data:
        for i in range(0,limit):
            headlines[i] = headlines[i].replace("'", "")
            headlines[i] = headlines[i].replace('"', "")
            print(headlines[i])
            speak(headlines[i])
    if 'terminal' in voice_data:
        comm = listen('What command')
        os.system(comm)

time.sleep(1)
while 1:
    voice_data = listen()
    respond(voice_data)