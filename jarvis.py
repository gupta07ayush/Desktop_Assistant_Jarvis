import pyttsx3

# sapi5 is a windows api which provides speech functions
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id) # two id available 0=David and 1=Zira
engine.setProperty('voice', voices[1].id)


# You can select any voice out of two.
# voices = engine.getProperty('voices')
# print(voices)
