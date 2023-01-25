import audioop
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[0].id)

def speak(audio):
    print('Devil\'s Rose: '+audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%H:%M:%p")
    speak(Time)

def today():
    Today=datetime.datetime.now().strftime("%A - %d/%m/%Y")
    speak(Today)

def Welcome():
    hour=datetime.datetime.now().hour
    if hour>=3 and hour<=10: 
        speak("Good Morning, Boss");
    elif hour>=11 and hour<=18: 
        speak("Good Afternoon, Boss")
    elif hour>=19 and hour<=24:
        speak("Good Night, Boss")
    speak("How can I help you")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print('Boss: '+query)
    except sr.UnknownValueError:
        speak("Please repeat or typing the command")
        query=str(input("Your order is: "))
    return query

if __name__ == "__main__":
    Welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google")
        elif "youtube" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Youtube")
        elif "open video" in query:
            file=os.path.realpath(r"D:\Album\Video laptop")
            os.startfile(file)
        elif "hi" in query or "hello" in query:
            speak("Hi, Boss")        
        elif "time" in query:
            time()
        elif "today" in query:
            today()
        elif "quit" in query or "goodbye" in query or "bye" in query:
            speak("Devil's Rose is quiting! Goodbye Boss")
            quit()
        else: 
            speak("Nothing, Sir")
        speak("How can I help you")