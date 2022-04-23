import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os
import webbrowser

import App_support


class Toplevel1:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
                top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        def age():
            os.system("python Age_and_Gender\main.py")

        def paint():
            os.system("python Virtual_Paint\Paint.py")

        def enhance():
            os.system("python Video_enhance\\video.py")

        def heart():
            os.system(
                "explorer http://localhost:5000/ & python Heart_Disease\\heart_disease_app.py")

        def content():
            webbrowser.open(
                "https://colab.research.google.com/drive/1xwTac3pAWLg6ELxPRgnkkM_UWMua17ag?usp=sharing", 1, autoraise=True)

        def feed():
            data = self.F_Box.get()
            blank = tk.StringVar()
            blank.set("")
            self.F_Box.configure(textvariable=blank)

            with open("feedback.txt", "r+") as f:
                sno = len(f.readlines())
                f.write(str(sno+1) + ". " + data + "\n")

        top.geometry("718x569+324+30")
        top.minsize(120, 1)
        top.maxsize(1359, 723)
        top.resizable(False, False)
        top.title("Processing.io")
        top.configure(background="#F3E9DD")

        self.top = top

        self.Headline = tk.Label(self.top)
        self.Headline.place(relx=-0.015, rely=-0.019, height=75, width=734)
        self.Headline.configure(background="#ff8000")
        self.Headline.configure(borderwidth="4")
        self.Headline.configure(compound='left')
        self.Headline.configure(disabledforeground="#a3a3a3")
        self.Headline.configure(
            font="-family {Neue Haas Grotesk Display Pro} -size 16 -weight bold -slant italic")
        self.Headline.configure(foreground="#FFF")
        self.Headline.configure(relief="raised")
        self.Headline.configure(text='''Processing.io''')

        self.Tagline = tk.Label(self.top)
        self.Tagline.place(relx=-0.017, rely=0.09, height=51, width=734)
        self.Tagline.configure(background="#FF6B6B")
        self.Tagline.configure(compound='left')
        self.Tagline.configure(cursor="arrow")
        self.Tagline.configure(disabledforeground="#a3a3a3")
        self.Tagline.configure(font="-family {Segoe UI} -size 12")
        self.Tagline.configure(foreground="#FFF")
        self.Tagline.configure(relief="ridge")
        self.Tagline.configure(
            text='''Welcome to processing.io! One stop solution for your favourite automation needs''')

        self.Instruction = tk.Label(self.top)
        self.Instruction.place(relx=-0.015, rely=0.179, height=47, width=736)
        self.Instruction.configure(background="#B6FFCE")
        self.Instruction.configure(compound='left')
        self.Instruction.configure(disabledforeground="#a3a3a3")
        self.Instruction.configure(font="-family {Segoe UI} -size 12")
        self.Instruction.configure(foreground="#000")
        self.Instruction.configure(
            text='''Make a choice and press the button''')

        self.App1 = tk.Button(self.top)
        self.App1.place(relx=0.045, rely=0.339, height=44, width=257)
        self.App1.configure(activebackground="#ececec")
        self.App1.configure(activeforeground="#000000")
        self.App1.configure(background="#4D96FF")
        self.App1.configure(borderwidth="4")
        self.App1.configure(compound='left')
        self.App1.configure(disabledforeground="#a3a3a3")
        self.App1.configure(
            font="-family {Gill Sans MT} -size 12 -weight bold")
        self.App1.configure(foreground="#fff")
        self.App1.configure(highlightbackground="#d9d9d9")
        self.App1.configure(highlightcolor="black")
        self.App1.configure(pady="0")
        self.App1.configure(text='''Age and Gender Classification''')
        self.App1.configure(command=age)

        self.App2 = tk.Button(self.top)
        self.App2.place(relx=0.561, rely=0.343, height=44, width=257)
        self.App2.configure(activebackground="#ececec")
        self.App2.configure(activeforeground="#000000")
        self.App2.configure(background="#4D96FF")
        self.App2.configure(borderwidth="4")
        self.App2.configure(compound='left')
        self.App2.configure(disabledforeground="#a3a3a3")
        self.App2.configure(
            font="-family {Gill Sans MT} -size 12 -weight bold")
        self.App2.configure(foreground="#fff")
        self.App2.configure(highlightbackground="#d9d9d9")
        self.App2.configure(highlightcolor="black")
        self.App2.configure(pady="0")
        self.App2.configure(text='''Virtual Paint''')
        self.App2.configure(command=paint)

        self.App3 = tk.Button(self.top)
        self.App3.place(relx=0.045, rely=0.478, height=44, width=257)
        self.App3.configure(activebackground="#ececec")
        self.App3.configure(activeforeground="#000000")
        self.App3.configure(background="#4D96FF")
        self.App3.configure(borderwidth="4")
        self.App3.configure(compound='left')
        self.App3.configure(disabledforeground="#a3a3a3")
        self.App3.configure(
            font="-family {Gill Sans MT} -size 12 -weight bold")
        self.App3.configure(foreground="#fff")
        self.App3.configure(highlightbackground="#d9d9d9")
        self.App3.configure(highlightcolor="black")
        self.App3.configure(pady="0")
        self.App3.configure(text='''Content Generator''')
        self.App3.configure(command=content)

        self.App4 = tk.Button(self.top)
        self.App4.place(relx=0.561, rely=0.478, height=44, width=257)
        self.App4.configure(activebackground="#ececec")
        self.App4.configure(activeforeground="#000000")
        self.App4.configure(background="#4D96FF")
        self.App4.configure(borderwidth="4")
        self.App4.configure(compound='left')
        self.App4.configure(disabledforeground="#a3a3a3")
        self.App4.configure(
            font="-family {Gill Sans MT} -size 12 -weight bold")
        self.App4.configure(foreground="#fff")
        self.App4.configure(highlightbackground="#d9d9d9")
        self.App4.configure(highlightcolor="black")
        self.App4.configure(pady="0")
        self.App4.configure(text='''Heart Disease Predictor''')
        self.App4.configure(command=heart)

        self.App5 = tk.Button(self.top)
        self.App5.place(relx=0.311, rely=0.619, height=44, width=257)
        self.App5.configure(activebackground="#ececec")
        self.App5.configure(activeforeground="#000000")
        self.App5.configure(background="#4D96FF")
        self.App5.configure(borderwidth="4")
        self.App5.configure(compound='left')
        self.App5.configure(disabledforeground="#a3a3a3")
        self.App5.configure(
            font="-family {Gill Sans MT} -size 12 -weight bold")
        self.App5.configure(foreground="#fff")
        self.App5.configure(highlightbackground="#d9d9d9")
        self.App5.configure(highlightcolor="black")
        self.App5.configure(pady="0")
        self.App5.configure(text='''FPS Enhanced Video Recording''')
        self.App5.configure(command=enhance)

        self.menubar = tk.Menu(top, font="TkMenuFont",
                               bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.menubar.add_command(
            compound="left",
            label="Menu")
        self.menubar.add_command(
            compound="left",
            label="About")
        self.menubar.add_command(
            compound="left",
            label="Help")
        self.menubar.add_command(
            compound="left",
            label="Quit")

        self.Feedback = tk.Label(self.top)
        self.Feedback.place(relx=0.125, rely=0.714, height=50, width=84)
        self.Feedback.configure(background="#F3E9DD")
        self.Feedback.configure(compound='left')
        self.Feedback.configure(cursor="fleur")
        self.Feedback.configure(disabledforeground="#a3a3a3")
        self.Feedback.configure(font="-family {Segoe UI} -size 12")
        self.Feedback.configure(foreground="#000000")
        self.Feedback.configure(text='''Feedback:''')

        self.F_Box = tk.Entry(self.top)
        self.F_Box.place(relx=0.139, rely=0.782, height=80, relwidth=0.507)
        self.F_Box.configure(background="white")
        self.F_Box.configure(disabledforeground="#a3a3a3")
        self.F_Box.configure(font="TkFixedFont")
        self.F_Box.configure(foreground="#000000")
        self.F_Box.configure(insertbackground="black")

        self.Sbut = tk.Button(self.top)
        self.Sbut.place(relx=0.682, rely=0.866, height=24, width=67)
        self.Sbut.configure(activebackground="#ececec")
        self.Sbut.configure(activeforeground="#000000")
        self.Sbut.configure(background="#d9d9d9")
        self.Sbut.configure(compound='left')
        self.Sbut.configure(disabledforeground="#a3a3a3")
        self.Sbut.configure(foreground="#000000")
        self.Sbut.configure(highlightbackground="#d9d9d9")
        self.Sbut.configure(highlightcolor="black")
        self.Sbut.configure(pady="0")
        self.Sbut.configure(text='''Submit''')
        self.Sbut.configure(command=feed)


def start_up():
    App_support.main()


if __name__ == '__main__':
    App_support.main()
