import tkinter as tk

top = tk.Tk()
top.geometry("1280x720")

list = ["hello", "hey", "test", "foo", "bar", "baz", "idk", "python", "c++", "java"]
word_dict = {}


def close(f):
    f()
    top.destroy()
    pass


def run(callback, quit):
    px = 50
    py = 50
    for word in list:
        if px > 1100:
            px = 50
            py += 200

        word_dict[word] = tk.Button(text=word, command=lambda j=word: callback(j))
        word_dict[word].place(bordermode=tk.OUTSIDE, height=100, width=100, x=px, y=py)
        px += 200

    quit_button = tk.Button(text='quit', command=lambda f=quit: close(f))
    quit_button.place(bordermode=tk.OUTSIDE, height=100, width=100, x=px, y=py)

    top.mainloop()
    pass


