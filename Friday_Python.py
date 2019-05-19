import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import sys
import os
import smtplib
import ctypes
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    

    if hour>= 0 and hour<12:
        speak("Good Morning Boss")
       
    elif hour>=12 and hour<16:
        speak("Good Afternoon Boss")
        
    else:
        speak("Good Evening Boss")
        

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query





if __name__ ==  "__main__":
    wishme()
    while True:
       query =  takeCommand().lower()
       if 'friday' in query:
            if 'wikipedia' in query:
               speak("Searching WIkipedia...")
               query = query.replace("wikipedia","")
               query = query.replace("friday","")
               results = wikipedia.summary(query,sentences = 2)
               speak("According to Wikipedia")
               print(results)
               speak(results)
               

            if  'play' in query:
                try:
                    search_query= query.split("play",1)[1]
                    url = "https://www.youtube.com/results?search_query=" + search_query
                    source_code = requests.get(url)
                    plain_text = source_code.text
                    soup = BeautifulSoup(plain_text,"html.parser")
                    songs = soup.findAll('div', {'class': 'yt-lockup-video'})
                    song = songs[0].contents[0].contents[0].contents[0]
                    hit = song['href']  
                    speak(f"Playing{search_query} on Youtube...")
                    webbrowser.open("https://www.youtube.com" + hit)

                except Exception as e:
                    print(str(e))


            if 'search' in query:
                search_query = query.split("search",1)[1]
                speak("Here's what I found on the web...")
                webbrowser.open("https://www.google.co.in/search?q=" + search_query)
            
            if 'exit' in query:
                speak("Bye boss")
                sys.exit()

            if 'stackoverflow' in query:
                speak("Opening stackoverflow...")
                webbrowser.open("stackoverflow.com")

            if 'play music' in query:
                speak("Playing music...")
                music_dir = "C:\\Users\\HP\\Desktop\\Extras\\music"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))    

            if 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Time is {strTime}")
            
            if 'open code' in query:
                codePath = "C:\\Program Files\\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

    
            if 'lock device' in query:
                try:
                    speak("locking the device...")
                    ctypes.windll.user32.LockWorkStation()
                except Exception as e:
                    print(str(e))



