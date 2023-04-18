from gpiozero import PWMLED, Button
from signal import pause
from time import sleep


rval = 1
gval = 1
bval = 1

R = PWMLED(14)
G = PWMLED(15)
B = PWMLED(18)

rbtn = Button(16)
gbtn = Button(20)
bbtn = Button(21)


def flash():

def r_go():
    global rval
    rval+=0.1
    if(rval>1):
        flash()
def g_go():
    global gval
    gval+=0.1
    if(gval>1):
        flash()
def b_go():
    global bval
    bval+=0.1
    if(bval>1):
        flash()


rbtn.when_pressed = r_go
gbtn.when_pressed = g_go
bbtn.when_pressed = b_go




while True :
    for i in range(10):
        R.value = i/10
        G.value = (1-i / 10)
        B.value = i / 10
        sleep(0.5)