import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

# sapi5 is a windows api which provides speech functions
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print how many voices available.
# voices = engine.getProperty('voices')
# print(voices)

# print(voices[0].id) # two id available 0=David and 1=Zira
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir, Please tell me how may I help you?")


def takeCommand():
    ''' It take microphone input from the user and returns string output.'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.6
        r.energy_threshold = 600
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return 'None'
    return query


if __name__ == "__main__":
    # wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia..")
            print(results)
            speak(results)

        # open websites
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open insta' in query:
            webbrowser.open("instagram.com/gupta07ayush")
        elif 'open github' in query:
            webbrowser.open("github.com/gupta07ayush")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com/in/gupta07ayush")
        elif 'open silver github' in query:
            webbrowser.open("github.com/AayushSilarpuria")

        # Play Music
        elif 'play music' in query:
            music_dir = "C:\\Users\\gupta\\OneDrive\\Desktop\\songs"
            songs = os.listdir(music_dir)
            songs_obj = (enumerate(songs, 1))
            for song in songs_obj:
                print((song))
            shuffle_no = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[shuffle_no]))

        # Current Time
        elif 'the time' in query:
            CurrentTime = datetime.datetime.now().strftime("%H:%M")
            print(CurrentTime)
            speak(f"Sir, the time is {CurrentTime}")

        # Open App
        elif "open code" in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # Exit loop
        elif 'baby exit' in query:
            print("Exiting the program")
            exit()
