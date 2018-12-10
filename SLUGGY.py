from sense_hat import SenseHat
sense = SenseHat()

slug = ([2, 4], [3, 4], [4, 4], [5, 4])

white = (255, 255, 255)

direction = "right"
blank = (0, 0, 0)
sleep(0.5)

def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], white)

def move():
    

sense.clear()
draw_slug()
        
