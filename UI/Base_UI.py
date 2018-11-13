from TTS.TTS import speak
from TTS.Reporter import report, close_report
import tkinter as tk
from Utility.Function_Mappings import get_mapping, set_mapping
from UI.Profile_Manager import load, save


def talk(**kwargs):
    speak(kwargs['text'])
    report(kwargs['text'])
    pass


def close(**kwargs):
    speak('goodbye')
    close_report()
    save(profile, 'test.txt')
    top.destroy()
    pass


def run():
    default_px = width / 20
    default_py = height / 20
    px = default_px
    py = default_py

    for text, function_key in profile.items():
        button = tk.Button(text=text, command=lambda w=text, key=function_key: get_mapping(key)(text=w))
        button.place(bordermode=tk.OUTSIDE, height=button_height, width=button_width, x=px, y=py)
        px += button_width
        if px > width - button_width:
            px = default_px
            py += button_height

    top.mainloop()
    pass


top = tk.Tk()
width = top.winfo_screenwidth()
height = top.winfo_screenheight()
button_height = height / 10
button_width = width / 10
top.geometry(str(width) + 'x' + str(height))

profile = load('test.txt')
set_mapping('Speak', talk)
set_mapping('Quit', close)
