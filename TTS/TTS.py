from gtts import gTTS
import os
from sys import platform
import pyttsx3


engine = pyttsx3.init()
if platform == 'linux' or platform == 'linux2':
    pass

elif platform == 'darwin':
    media_cmd = 'afplay '

elif platform == 'win32':
    media_cmd = 'start '


def speak(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        sf = 'temp.mp3'
        tts.save(sf)
        os.system(media_cmd + sf)
        os.remove(sf)
    except:
        engine.say(text)
        engine.runAndWait()
    pass
