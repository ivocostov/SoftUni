from tkinter import Tk, Canvas


def create_root():
    root = Tk()  #

    root.title("My first Tkinter exercise")  # window title
    root.resizable(False, False)  # making window not resizable
    root.geometry("700x600")  # size of window

    return root

    #root.mainloop()  # used if no function


def create_frame():  # creating invisible layer on top of window
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)  # this is top left corner

    return frame


root = create_root()
frame = create_frame()