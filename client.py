import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image
import random

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None
canvas2 = None

playerName = None
nameEntry = None
nameWindow = None
gamewindow = None
rollButton = None
dice = None
playerType = None
playerTurn = None
player1Turn = None
player2Turn = None
leftBoxes = []
rightBoxes = []
finishBoxes = None


# Teacher write code here for askPlayerName()


def askPlayerName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    nameWindow = Tk()
    nameWindow.title("Ludo ladder game")
    nameWindow.attributes('-fullscreen', True)

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="assets/background.png")

    canvas1 = Canvas(nameWindow, width=500, height=500)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.create_text(screen_width/2, screen_height/5,
                        text="Ludo Ladder Game", font=("Chalkboard SE", 100), fill="white")

    nameEntry = Entry(nameWindow, width=10, justify="center",
                      font=("Chalkboard SE", 100), bg="white")
    nameEntry.place(x=screen_width/2-370, y=screen_height/4+100)

    button = Button(nameWindow, text="save", font=(
        "Chalkboard SE", 40), bg="grey", bd=3, width=5, command=saveName)
    button.place(x=screen_width/2-120, y=screen_height/2+100)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()


def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()
    playWindow()
    SERVER.send(playerName.encode("utf-8"))


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    # Creating First Window
    askPlayerName()


def playWindow():
    global SERVER
    global gamewindow
    global canvas2
    global screen_width
    global screen_height
    global dice
    global rollButton
    global playerName
    global playerType
    global playerTurn

    gamewindow = Tk()
    gamewindow.title("Ludo game")
    gamewindow.attributes("-fullscreen", True)

    screen_width = gamewindow.winfo_screenwidth()
    screen_height = gamewindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file="assets/background.png")

    canvas2 = Canvas(gamewindow, width=screen_width, height=500)
    canvas2.pack(fill="both", expand=True)

    canvas2.create_image(0, 0, image=bg, anchor="nw")
    canvas2.create_text(screen_width/2, screen_height/5,
                        text="Ludo game", font=("Chalkboard SE", 100), fill="white")

    leftBoard()
    rightBoard()
    finishLine()

    rollButton = Button(gamewindow, text="Roll the dice", bg="lightcyan", fg="black", font=(
        "monospace", 15), width=20, height=2, command=rollingButton)
    rollButton.place(x=screen_width/2-120, y=screen_height/2+280)

    dice = canvas2.create_text(screen_width/2-10, screen_height /
                               2+185, text="\u2680", font=("monospace", 200), fill="white")

    gamewindow.resizable(True, True)

    gamewindow.mainloop()


def leftBoard():
    global gamewindow
    global leftBoxes
    global screen_width
    global screen_height
    x1 = 10
    for i in range(0, 11):
        if i == 0:
            box_label = Label(gamewindow, width=1, height=1,
                              borderwidth=2, bg="red", font=("Chalkboard SE", 30))
            box_label.place(x=x1, y=screen_height/2-30)
            leftBoxes.append(box_label)
            x1 += 30
        else:
            box_label = Label(gamewindow, width=1, height=1,
                              borderwidth=2, bg="white", font=("Chalkboard SE", 30))
            box_label.place(x=x1, y=screen_height/2-30)
            leftBoxes.append(box_label)
            x1 += 50


def rightBoard():
    global gamewindow
    global rightBoxes
    global screen_width
    global screen_height
    x2 = 748
    for i in range(0, 11):
        if i == 10:
            box_label = Label(gamewindow, width=1, height=1,
                              borderwidth=2, bg="green", font=("Chalkboard SE", 30))
            box_label.place(x=x2, y=screen_height/2-30)
            rightBoxes.append(box_label)
            x2 += 30
        else:
            box_label = Label(gamewindow, width=1, height=1,
                              borderwidth=2, bg="white", font=("Chalkboard SE", 30))
            box_label.place(x=x2, y=screen_height/2-30)
            rightBoxes.append(box_label)
            x2 += 50


def finishLine():
    global gamewindow
    global finishBoxes
    global screen_width
    global screen_height
    finishBoxes = Label(gamewindow, width=8, height=4, text="HOME",
                        bg="brown", fg="white", font=("Chalkboard SE", 30))
    finishBoxes.place(x=screen_width/2-100, y=screen_height/2-100)


def rollingButton():
    global SERVER
    global playerType
    global playerTurn
    global rollButton
    diceFace = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    value = random.choice(diceFace)
    print(value)
    # if playerType == "player1":
    #     SERVER.send(f"{value}player2Turn".encode("utf-8"))
    # elif playerType == "player2":
    #     SERVER.send(f"{value}player1Turn".encode("utf-8"))


setup()
