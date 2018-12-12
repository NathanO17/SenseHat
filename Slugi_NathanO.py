from sense_hat import SenseHat
sense = SenseHat()
from time import *

slug = [[3, 4], [4, 4], [5, 4]]

cyan = (0, 255, 255)

direction = "right"
blank = (0, 0, 0)

def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], cyan)

def move():
    last = slug[-1]
    first = slug[0]
    next = list(last)
    if direction == "right":
        if last[0] + 1 == 8:
            next[0] = 0
        else:
            next[0] = last[0] + 1
            
    elif direction == "left":
        if last[0] - 1 == -1:
            next[0] = 7
        else:
            next[0] = last[0] - 1

    elif direction == "down":
        if last[1] + 1 == 8:
            next[1] = 0
        else:
            next[1] = last[1]

            



    slug.append(next)
    sense.set_pixel(next[0], next[1], cyan)
    sense.set_pixel(first[0], first[1], blank)
    slug.remove(first)

     
        

while True:
    sleep(0.5)
    draw_slug()
    move()
