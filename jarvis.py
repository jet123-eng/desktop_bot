import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning jesica ")
    elif(hour>=12 and hour<=18):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am GINNIE, how may i help you")
def takeCommand():

    ''' takes microphone input from user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold= 1
        '''pause threshold=number of seconds the system will take to recognize the voice after the user has completed their sentence'''
        audio=r.listen(source)
        
        
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User Said:",query)
    except Exception as e:
        print("Say that again please.........")
        return "none"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing tasks based on query
        if "wikipedia" in query:
            print("Searching wikipedia")
            query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir="D:\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs))]))
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%Hhours%Mminutes%Sseconds")
            speak(f"the time is{strTime}")
        
