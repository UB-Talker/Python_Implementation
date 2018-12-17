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


'''
Called by the 'Add' Button. Makes a call to the add_button_popup function to ask the user what they want their 
new Button to do. The 'Hello' and 'World!' buttons were added using this new functionality.
'''
def add(**kwargs):
    global max_px
    global max_py
    new_button_params = add_button_popup()
    b_text = new_button_params['new_button_text']
    b_type = new_button_params['new_button_type']
    b = tk.Button(text=b_text, command=lambda w=b_text, key=b_type: get_mapping(key)(text=w))
    if max_px > width - button_width:
        max_px = width / 20
        max_py += button_height
    b.place(bordermode=tk.OUTSIDE, height=button_height, width=button_width, x=max_px, y=max_py)
    max_px += button_width
    profile[b_text] = b_type
    save(profile, 'test.txt')


'''
Displays a pop up so the user may input what they want their new button to do
'''
def add_button_popup(**kwargs):
    ret_val = {'new_button_type': None, 'new_button_text': None}
    popup = tk.Tk()
    popup.geometry(str(400) + 'x' + str(150))

    tk.Label(popup, text='Please enter a name for the button: ').pack()

    text = tk.Entry(popup)
    text.pack()

    new_button_type = tk.StringVar()
    new_button_type.set('Speak')
    speech_button = tk.Radiobutton(popup, indicatoron=0, variable=new_button_type, value='Speak', text='Add a speech button')
    speech_button.pack()
    folder_button = tk.Radiobutton(popup, indicatoron=0, variable=new_button_type, value='Folder', text='Add a folder button')
    folder_button.pack()

    def submit():
        ret_val['new_button_type'] = new_button_type.get()
        ret_val['new_button_text'] = text.get()
        popup.quit()

    tk.Button(popup, text='Submit', command=submit).pack()
    popup.mainloop()
    popup.destroy()
    return ret_val


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

    global max_px
    max_px = px
    global max_py
    max_py = py

    top.mainloop()
    pass


top = tk.Tk()
width = top.winfo_screenwidth()
height = top.winfo_screenheight()
button_height = height / 10
button_width = width / 10
max_px = 0
max_py = 0
top.geometry(str(width) + 'x' + str(height))

profile = load('test.txt')
set_mapping('Speak', talk)
set_mapping('Quit', close)
set_mapping('Add', add)
