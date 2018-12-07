import pyttsx3
import platform


def speak(text):
    engine.say(text)
    engine.runAndWait()


engine = pyttsx3.init()
if platform.system() == "Windows":
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #Set voice to default male voice in sapi5
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 25) #slow the speed of the voice to sound more natural