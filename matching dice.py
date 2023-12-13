import tkinter as tk
import random
import time
WIDTH = 800
HEIGHT = 800

window = tk.Tk()
canvas = tk.Canvas(width = WIDTH, height = HEIGHT ,bg = 'white')
canvas.pack()

def create_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    x = 50
    y = 400
    canvas.create_rectangle(x,x,x+300,x+300)
    canvas.create_rectangle(y,x,y+300,x+300)

    if dice_1 == 1:
        canvas.create_oval(x+75,x+75,x+225,x+225,fill="black")
    elif dice_1 == 2:
        canvas.create_oval(x+25,x+25,x+125,x+125,fill="black")
        canvas.create_oval(x+175,x+175,x+275,x+275,fill="black")
    elif dice_1 == 3:
        canvas.create_oval(x+25,x+25,x+125,x+125,fill="black")
        canvas.create_oval(x+175,x+175,x+275,x+275,fill="black")
        canvas.create_oval(x+100,x+100,x+200,x+200,fill="black")
    elif dice_1 == 4:
        canvas.create_oval(x+25,x+25,x+125,x+125,fill="black")
        canvas.create_oval(x+175,x+25,x+275,x+125,fill="black")
        canvas.create_oval(x+25,x+175,x+125,x+275,fill="black")
        canvas.create_oval(x+175,x+175,x+275,x+275,fill="black")
    elif dice_1 == 5:
        canvas.create_oval(x+25,x+25,x+100,x+100,fill="black")
        canvas.create_oval(x+200,x+25,x+275,x+100,fill="black")
        canvas.create_oval(x+25,x+200,x+100,x+275,fill="black")
        canvas.create_oval(x+200,x+200,x+275,x+275,fill="black")
        canvas.create_oval(x+112.5,x+112.5,x+187.5,x+187.5,fill="black")
    elif dice_1 == 6:
        canvas.create_oval(x+25,x+25,x+100,x+100,fill="black")
        canvas.create_oval(x+200,x+25,x+275,x+100,fill="black")
        canvas.create_oval(x+25,x+200,x+100,x+275,fill="black")
        canvas.create_oval(x+200,x+200,x+275,x+275,fill="black")
        canvas.create_oval(x+25,x+112.5,x+100,x+187.5,fill="black")
        canvas.create_oval(x+200,x+112.5,x+275,x+187.5,fill="black")



    if dice_2 == 1:
        canvas.create_oval(y+75,x+75,y+225,x+225,fill="black")
    elif dice_2 == 2:
        canvas.create_oval(y+25,x+25,y+125,x+125,fill="black")
        canvas.create_oval(y+175,x+175,y+275,x+275,fill="black")
    elif dice_2 == 3:
        canvas.create_oval(y+25,x+25,y+125,x+125,fill="black")
        canvas.create_oval(y+175,x+175,y+275,x+275,fill="black")
        canvas.create_oval(y+100,x+100,y+200,x+200,fill="black")
    elif dice_2 == 4:
        canvas.create_oval(y+25,x+25,y+125,x+125,fill="black")
        canvas.create_oval(y+175,x+25,y+275,x+125,fill="black")
        canvas.create_oval(y+25,x+175,y+125,x+275,fill="black")
        canvas.create_oval(y+175,x+175,y+275,x+275,fill="black")
    elif dice_2 == 5:
        canvas.create_oval(y+25,x+25,y+100,x+100,fill="black")
        canvas.create_oval(y+200,x+25,y+275,x+100,fill="black")
        canvas.create_oval(y+25,x+200,y+100,x+275,fill="black")
        canvas.create_oval(y+200,x+200,y+275,x+275,fill="black")
        canvas.create_oval(y+112.5,x+112.5,y+187.5,x+187.5,fill="black")
    elif dice_2 == 6:
        canvas.create_oval(y+25,x+25,y+100,x+100,fill="black")
        canvas.create_oval(y+200,x+25,y+275,x+100,fill="black")
        canvas.create_oval(y+25,x+200,y+100,x+275,fill="black")
        canvas.create_oval(y+200,x+200,y+275,x+275,fill="black")
        canvas.create_oval(y+25,x+112.5,y+100,x+187.5,fill="black")
        canvas.create_oval(y+200,x+112.5,y+275,x+187.5,fill="black")
    time.sleep(1)

while True:
    create_dice()


    
    






window.mainloop()