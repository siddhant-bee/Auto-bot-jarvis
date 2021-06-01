import pyttsx3 as pt
import datetime as dt
import speech_recognition as sr 
import wikipedia
import webbrowser as wb
import os 
import pyautogui 
import psutil

from wikipedia.wikipedia import search

engine = pt.init()
voices=engine.getProperty("voices")
rate=engine.getProperty("rate")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 180)



#speak
def speak(audio):

    engine.say(audio)
    engine.runAndWait()
#time    
def time( ):
    time=dt.datetime.now().strftime("%I:%M:%S")
    speak("time is ")
    speak(time)
#time()  
#year
def date():
    year=int(dt.datetime.now().year)
    month=int(dt.datetime.now().month)
    day=int(dt.datetime.now().day)
    speak("the date is")
    speak(day)
    speak(month)
    speak(year)

#date()
#greet
def wish_me():
    
    hour=dt.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak ("Good morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak(" sir i m glad you are here")
    speak("jarvis at your service sir ")
#wish_me()    

#cpu
def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at " + usage )
    battery = psutil.sensors_battery   
    speak("we have enoug fule sir we have only " + battery.percent + " percent ")
         

 #take command
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listning sir ....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google (audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"
    return query

#take_command()   




if __name__ == "__main__" : 

    wish_me()

    while True:
        query = take_command() . lower()
        print(query)
        if "time" in query:
            time( )
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("ok sir bye")
            print("ok sir bye.....")
            quit()
        elif "wikipedia" in query:
            speak("searching for your query sir please wait ")
            query=query.replace("wikipedia", "")
            result= wikipedia.summary(query,sentences = 2)
            speak(result)    
        elif "chrome" in query:
            speak("what should i search sir")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search=take_command().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1") 
        elif "restart" in query:
            os.system("shutdown /r /t 1")   
        elif "song" in query:
            songs_dir="c:\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))   
        elif "remember" in query:
            speak("what should i remeber ")
            data=take_command()
            speak("you said me to remember" + data )
            remeber=open("data.txt", "w")
            remeber.write(data)
            remeber.close()            
        elif"tell" in query:
            remeber = open("data.txt", "r")
            speak("you told me" + remeber.read()) 
        elif "cpu" in query:
            cpu()
    