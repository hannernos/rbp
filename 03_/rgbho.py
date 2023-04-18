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
    global rval, gval, bval, R, G, B
    R.value = rval
    G.value = gval
    B.value = bval


def r_go():
    global rval
    rval += 0.1
    if rval > 1:
        rval = 0
    flash()


def g_go():
    global gval
    gval += 0.1
    if gval > 1:
        gval = 0
    flash()


def b_go():
    global bval
    bval += 0.1
    if bval > 1:
        bval = 0
    flash()


flash()

rbtn.when_pressed = r_go
gbtn.when_pressed = g_go
bbtn.when_pressed = b_go

pause()
