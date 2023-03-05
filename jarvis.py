import pyttsx3
import datetime

# sapi5 is a windows api which provides speech functions
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

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


# print how many voices available.
# voices = engine.getProperty('voices')
# print(voices)
if __name__ == "__main__":
    speak("harry is a good boy")
