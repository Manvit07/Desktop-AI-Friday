import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M")

def get_day():
    current_day = datetime.datetime.now()
    return current_day.strftime("%A")

def get_date():
    return datetime.datetime.now().strftime('%d %B %Y')

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Boss!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("Friday at your service, how may I help you today?")

def calendar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        status = r.recognize_google(audio, language='en-in')
        print(f"User said: {status}\n")
    except Exception as e:
        print("Say that again please...")
        return "none"
    return status

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "none"
    return query.lower()


if __name__ == "__main__":
    wish_me()
    
    while True:
        query = take_command()

        if 'open youtube' in query:
            speak("Just a second sir, opening YouTube...")
            webbrowser.open("https://www.youtube.com/")
            speak("Here you go sir. Anything else I can help you with?")

        elif 'song' in query:
            speak("Yes boss! Lights, camera, and music...")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=6FhTvzY5bxs")
            speak("Enjoy your playlist sir. Anything else I can assist you with?")

        elif "playlist" in query:
            speak("Alright boss...")
            music_dir = ''# put your music file address here to listen downloaded songs 
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing your favorite music. Anything else you'd like?")

        elif 'friday stop' in query or any(keyword in query for keyword in ["close", "shut down", "sleep"]):
            speak("Alright sir, with your permission...")
            speak("Have a nice day sir!")
            break
