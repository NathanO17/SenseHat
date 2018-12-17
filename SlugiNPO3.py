from sense_hat import SenseHat
sense = SenseHat()
from time import *
from random import randint
from random import *

slug = [[3, 4], [4, 4], [5, 4]]
direction = "right"
cyan = (0, 255, 255)
blank = (0, 0, 0)
green = (0, 0, 255)

sense.set_pixel(2, 4, blank)
sense.set_pixel(3, 4, cyan)
sense.set_pixel(4, 4, cyan)
vegetables = []
score = 0

def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], cyan)

def move():
    remove = True
    global score
    last = slug[-1]
    first = slug[0]
    next = list(last)
    if remove is True:
        sense.set_pixel(first[0], first[1], blank)
        slug.remove(first)
        
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
            next[1] = last[1] + 1

    elif direction == "up":
        if last[1] - 1 == -1:
            next[1] = 7
        else:
            next[1] = last[1] - 1
    if next in vegetables:
        vegetables.remove(next)
        score += 1
            
    slug.append(next)
    sense.set_pixel(next[0], next[1], cyan)
    sense.set_pixel(first[0], first[1], blank)
    

def joystick_moved(event):
    global direction
    direction = event.direction

def make_veg():
    new = slug[0]
    while new in slug:
        x = randint(0, 7)
        y = randint(0, 7)
        new = [x, y]
    vegetables.append(new)
    sense.set_pixel(x, y, 255, 255, 255)


sense.clear()

while True:
    sleep(0.5)
    draw_slug()
    move()
    sense.stick.direction_any = joystick_moved
    if len(vegetables) < 3:
        make_veg()
