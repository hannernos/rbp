from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
from signal import pause

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED: y-=1

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED: y+=1

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED: x-=1


def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED: x+=1

def refresh():
    sense.clear()
    sense.set_pixel(x,y,255,255,255)

x=3
y=3

sense = SenseHat()

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh

pause()

