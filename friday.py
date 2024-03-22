import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now()
    Time = current_time.strftime("%H:%M")
    return Time

def get_day():
    current_day = datetime.datetime.now()
    day_of_week = current_day.strftime("%A")
    return day_of_week

def get_date():
    DATE = datetime.datetime.now().strftime('%B')
    date = datetime.datetime.now().strftime(f'%d {DATE} %Y')
    return date


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening Boss!")

    speak("i am friday , how may i help you today...")

def calender():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        status = r.recognize_google(audio, language='en-in')
        print(f"user said: {status}\n")
    except Exception as e:
        print("say that again please...")
        return "none"
    return status

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please...")
        return "none"
    return query


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak(f"searching wikipedia...  ")
            results = wikipedia.summary(query, sentences = 2)
            speak(f"according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak(f"opening youtube...  ")
            webbrowser.open("youtube.com")
        
        elif 'playlist' in query:
            speak(f"yes boss!. lights camera and music...")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=YR12Z8f1Dh8&list=PLb0Wdm54HWRx0Itb6yWfuDxMn2AXozmfS")

        elif "music" in query:
            speak(f'all right boss!...')
            music_dir = 'D:\\my songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0] ))
            
else:
       status = calender().lower()

       if "time" in status:
            TIME = get_time()
            speak(f"sir , the time is {TIME}")

       elif 'date' in status:
            DATE = get_date()
            speak(f"sir , today's date is {DATE}")
        
       elif 'day' in status:
            DAY = get_day()
            speak(f"sir , today's day is {DAY}")

  
    
       
       

        
            
        
        


        