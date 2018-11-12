import tkinter as tk


top = tk.Tk()
width = top.winfo_screenwidth()
height = top.winfo_screenheight()
button_height = height / 10
button_width = width / 10
top.geometry(str(width) + 'x' + str(height))

list = ["hello", "hey", "test", "foo", "bar", "baz", "idk", "python", "c++", "java"]
word_dict = {}


def close(f):
    f()
    top.destroy()
    pass


def run(callback, quit):
    default_px = width / 20
    default_py = height / 20
    px = default_px
    py = default_py

    for word in list:

        word_dict[word] = tk.Button(text=word, command=lambda w=word: callback(w))
        word_dict[word].place(bordermode=tk.OUTSIDE, height=button_height, width=button_width, x=px, y=py)
        px += button_width
        if px > width - button_width:
            px = default_px
            py += button_height

    quit_button = tk.Button(text='quit', command=lambda f=quit: close(f))
    quit_button.place(bordermode=tk.OUTSIDE, height=button_height, width=button_width, x=px, y=py)

    top.mainloop()
    pass


