from TTS.TTS import speak
from TTS.Reporter import report, close_report
from UI.base_ui import run


def callback(text):
    speak(text)
    report(text)
    pass


def close_op():
    speak('goodbye')
    close_report()
    pass


if __name__ == '__main__':
    run(callback, close_op)
