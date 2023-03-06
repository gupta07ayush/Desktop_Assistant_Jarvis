import pyttsx3
import datetime
import speech_recognition as sr

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
        return "None"


if __name__ == "__main__":
    wishMe()
    takeCommand()
