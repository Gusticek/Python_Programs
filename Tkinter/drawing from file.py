from tkinter import *
points = []
with open(r"X:\IV. FG\\Point Files\points1.txt", encoding = 'utf-8') as source_file:

    for line in source_file:
        coords = line.split()
        x = int(coords[0])
        y = int(coords[1])
        coords = [x,y]
        points.append(coords)
        
            
window = Tk()
canvas = Canvas(window, width = 500, height = 500)
canvas.pack()

for point in points:
    x, y = point[0], point[1]
    canvas.create_oval(x-2,y-2,x+2,y+2)
    canvas.create_line(points)
   

window.mainloop()
 