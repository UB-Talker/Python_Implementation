from gtts import gTTS
import pyttsx3
from pygame import mixer
from io import BytesIO

engine = pyttsx3.init()
mixer.init()


def speak(text, lang='en'):

    try:
        tts = gTTS(text=text, lang=lang)
        sf = BytesIO()
        tts.write_to_fp(sf)
        sf.seek(0)
        mixer.music.load(sf)
        mixer.music.play()
    except:
        engine.say(text)
        engine.runAndWait()
    pass
