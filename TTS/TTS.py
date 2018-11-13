from gtts import gTTS
from gtts.tts import gTTSError
from ttslib import tts as local_tts
from pygame import mixer
from io import BytesIO
import socket


def internet_connected():
    try:
        socket.gethostbyname('www.google.com')
        return True
    except socket.gaierror:
        return False


def speak(text, lang='en'):
    try:
        gtts = gTTS(text=text, lang=lang)
        sf = BytesIO()
        gtts.write_to_fp(sf)
        sf.seek(0)
        mixer.music.load(sf)
        mixer.music.play()
    except gTTSError:
        local_tts(text, 'en')
    pass


mixer.init()
