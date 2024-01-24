import tkinter as tk
import random
import time

WIDTH = 575
HEIGHT = 575

window = tk.Tk()
canvas = tk.Canvas(width = WIDTH, height = HEIGHT ,bg = 'white')
canvas.pack()

list1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
random.shuffle(list1)
# print(list1)
stvorce = []
coords = []
last_square = 0
square = 0
counter = 0
def pexeso():
    x = 50
    y = 50
    cislo = 0
    for i in range(4):
        for i in range(4):
            canvas.create_rectangle(x,y,x+100,y+100)
            stvorce.append(cislo)
            coords.append([x,y])
            x+=125
            cislo +=1
        y+=125
        x=50
def click(coordinates):
    global counter,last_square,last_square1,heavy_counter
    for i in range(16):
        if coordinates.x in range(coords[i][0],coords[i][0]+100) and coordinates.y in range(coords[i][1],coords[i][1]+100):
#             print(i)
            canvas.create_text(coords[i][0]+50,coords[i][1]+50,text=list1[i])
#             print(counter)
#             print(counter%2)
            if  counter%2 == 1:
                    if list1[square] == list1[last_square]:
                        pass
                    else:
                        canvas.after(1000,flip(i,last_square))
            print(last_square)
            last_square = i
            counter+=1
def flip(x,y):
    canvas.create_rectangle(coords[x][0],coords[x][1],coords[x][0]+100,coords[x][1]+100,fill = 'white')
    canvas.create_rectangle(coords[y][0],coords[y][1],coords[y][0]+100,coords[y][1]+100,fill = 'white')
    print(square)


pexeso()
print(coords)
canvas.bind('<Button-1>',click)




window.mainloop()