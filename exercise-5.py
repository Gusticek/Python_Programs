import tkinter as tk



count = 0
counter = 0


WIDTH = 800
HEIGHT = 800
x1 = 150
x2 = 650
y1 = 50
y2 = 250
colours = ['blue', 'red', 'green', 'yellow']
colors = ['orange', 'purple', 'grey', 'yellow']
window = tk.Tk()
canvas = tk.Canvas(width = WIDTH, height = HEIGHT ,bg = 'white')
canvas.pack()
canvas.create_rectangle(x1,y1,x2,y2,fill = 'white')

def change_color(coordinates):
    global count,counter
    if coordinates.x in range(x1,x2) and coordinates.y in range(y1,y2):
        counter+=1
        if counter == 4:
            counter = 0
    else:
        count+=1
        if count == 4:
            count = 0
            
    canvas.create_rectangle(0,0,WIDTH,HEIGHT,fill = colors[count])
    canvas.create_rectangle(x1,y1,x2,y2,fill = colours[counter])
canvas.bind('<Button-1>',change_color)

window.mainloop()