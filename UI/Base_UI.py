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
    profile[current_folder][b_text] = b_type
    if b_type == 'Folder':
        profile[b_text] = {'Home': 'Folder', 'Quit': 'Quit', 'Add a new button to\n the ' + str(b_text) + ' folder': 'Add'}
    save(profile, 'test.txt')


'''
Displays a pop up so the user may input what they want their new button to do
'''
def add_button_popup(**kwargs):
    ret_val = {'new_button_type': None, 'new_button_text': None}
    popup = tk.Tk()
    popup.geometry('400x150')

    tk.Label(popup, text='Please enter a name for the button: ').pack()

    text = tk.Entry(popup)
    text.pack()

    new_button_type = tk.StringVar(popup)
    speech_button = tk.Radiobutton(popup, indicatoron=0, variable=new_button_type, value='Speak', text='Add a speech button')
    speech_button.pack()
    folder_button = tk.Radiobutton(popup, indicatoron=0, variable=new_button_type, value='Folder', text='Add a folder button')
    folder_button.pack()

    def submit():
        if new_button_type.get() == 'Folder' and text.get() in profile:
            warning = tk.Message(popup, text="There already exists a folder with this name. Please choose a different name", fg="red")
            warning.pack()
            popup.geometry('400x250')
            popup.mainloop()
        else:
            ret_val['new_button_type'] = new_button_type.get()
            ret_val['new_button_text'] = text.get()
            popup.quit()

    tk.Button(popup, text='Submit', command=submit).pack()
    popup.mainloop()
    popup.destroy()
    return ret_val


def place_folder_buttons(folder_name):
    default_px = width / 20
    default_py = height / 20
    px = default_px
    py = default_py

    for text, function_key in profile[folder_name].items():
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


def open_folder(**kwargs):
    while len(top.winfo_children()) > 4:
        i = len(top.winfo_children()) - 1
        top.winfo_children()[i].destroy()

    place_folder_buttons(kwargs['text'])
    global current_folder
    if 'button' not in kwargs:
        prev_folders.append(current_folder)
    if len(prev_folders) != 0:
        top.winfo_children()[1].config(state=tk.NORMAL)
    current_folder = kwargs['text']
    top.mainloop()


def back_button(**kwargs):
    global next_folders, current_folder, prev_folders
    next_folders.append(current_folder)
    current_folder = prev_folders.pop()
    if len(prev_folders) == 0:
        top.winfo_children()[1].config(state=tk.DISABLED)
    top.winfo_children()[2].config(state=tk.NORMAL)
    open_folder(text=current_folder, button='back')


def forward_button(**kwargs):
    global next_folders, current_folder, prev_folders
    prev_folders.append(current_folder)
    current_folder = next_folders.pop()
    if len(next_folders) == 0:
        top.winfo_children()[2].config(state=tk.DISABLED)
    top.winfo_children()[1].config(state=tk.NORMAL)
    open_folder(text=current_folder, button='forward')


def run():
    nav_button_width = button_width / 2
    nav_button_height = button_height / 2

    nav_buttons = {'Home': 'Folder',
                   '<-': 'Back',
                   '->': 'Forward',
                   'Quit': 'Quit'}

    px = 0
    for b_text, b_key in nav_buttons.items():
        button = tk.Button(text=b_text, command=lambda w=b_text, key=b_key: get_mapping(key)(text=w), foreground='green')
        button.place(bordermode=tk.OUTSIDE, height=nav_button_height, width=nav_button_width, x=px, y=0)
        px += nav_button_width

    top.winfo_children()[1].config(state=tk.DISABLED)
    top.winfo_children()[2].config(state=tk.DISABLED)
    top.winfo_children()[3].config(fg='red')

    place_folder_buttons('Home')
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

#These lists will be used as stacks for folder navigation
prev_folders = []
next_folders = []


profile = load('test.txt')
current_folder = 'Home'
set_mapping('Speak', talk)
set_mapping('Quit', close)
set_mapping('Add', add)
set_mapping('Folder', open_folder)
set_mapping('Back', back_button)
set_mapping('Forward', forward_button)
