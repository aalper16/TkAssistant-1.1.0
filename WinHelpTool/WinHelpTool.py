import tkinter as tk
import playsound
from PIL.ImageTk import PhotoImage
import pyautogui as pg
import time
import os
import webbrowser as web


os.system("title WinHelpTool SHELL")

def cmd():
    os.system("cmd")
    print("started COMMAND PROMPT")

def chrome():
    os.startfile("chrome.exe")
    print("started CHROME")

def xampp():
    os.chdir("C:/xampp")
    os.startfile("xampp-control.exe")
    print("started XAMPP CONTROL PANEL")

def python():
    os.startfile("python.exe")
    print("started PYTHON")

def settings():
    os.system("start ms-settings:")
    print("started ms-settings:")

def calc():
    os.system("calc")
    print("started CALCULATOR")

def brave():
    os.startfile("brave.exe")
    print("started BRAVE BROWSER")

def github():
    web.open_new_tab("https://github.com/")
    print("started GitHub")

def youtube():
    web.open_new_tab("https://youtube.com")
    print("started YouTube")


def vid():
    global vidname
    vid = tk.Tk()
    vid.title("VIDEO")
    vid.iconbitmap("video.ico")
    vid.geometry("200x200")
    vidname = tk.Label(vid, text = "VIDEO NAME: ", font = "Helvetica 8")
    vidname.pack()
    vidname = tk.Entry(vid, width = 20, font = "Helvetice 16")
    vidname.pack()
    ok = tk.Button(vid, text = "OK", font = "Helvetica 16", command = openvid)
    ok.pack()
    vid.mainloop()
    print("strated Video Player")


def openvid():
    global vidname
    web.open_new_tab("https://www.youtube.com/results?search_query=" + vidname.get())
    print("opened", vidname.get())


window = tk.Tk()
window.title("WinHelpTool")
window.iconbitmap("windows.ico")
window.geometry("700x100")
window.tk_setPalette("#FFFFFF")
img2 = tk.PhotoImage(file="CHROME.png")
img3 = tk.PhotoImage(file="xamppphoto.png")
img4 = tk.PhotoImage(file="python.png")
img5 = tk.PhotoImage(file="windows.png")
img6 = tk.PhotoImage(file="calc.png")
img7 = tk.PhotoImage(file="Brave_lion.png")
img8 = tk.PhotoImage(file="github.png")
img9 = tk.PhotoImage(file="youtube.png")
img10 = tk.PhotoImage(file="vid.png")


button2 = tk.Button(text = "CHROME", image = img2, compound="top", command = chrome)
button2.place(x = 10, y = 10)
button3 = tk.Button(text = "XAMPP", image = img3, compound = "top", command = xampp)
button3.place(x = 80, y = 10)
button4 = tk.Button(text = "PYTHON", image = img4, compound = "top", command = python)
button4.place(x = 150, y = 10)
button5 = tk.Button(text = "SETTINGS", image = img5, compound = "top", command = settings)
button5.place(x = 225, y = 10)
button6 = tk.Button(text = "CALCULATOR", image = img6, compound = "top", command = calc)
button6.place(x = 300, y = 10)
button7 = tk.Button(text = "BRAVE", image = img7, compound= "top", command = brave)
button7.place(x = 395, y = 10)
button8 = tk.Button(text = "GITHUB", image = img8, compound = "top", command = github)
button8.place(x = 470, y = 10)
button9 = tk.Button(text = "YOUTUBE", image = img9, compound = "top", command = youtube)
button9.place(x = 540, y = 10)
button10 = tk.Button(text = "VIDEO", image = img10, compound = "top", command = vid)
button10.place(x = 610, y = 10)

window.mainloop()