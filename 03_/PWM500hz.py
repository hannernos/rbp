from gpiozero import PWMLED, Button
from signal import pause
from time import sleep
#by sleep

R = PWMLED(2)
G = PWMLED(3)
B = PWMLED(4)

rbtn = Button(16)
gbtn = Button(20)
bbtn = Button(21)

rval=1
gval=1
bval=1
def flash():
    global rval, gval, bval, R,G,B
    R.value = rval
    G.value = gval
    B.value = bval
def a_on():
    global rval, gval, bval, R,G,B
    rval = 1
    gval = 1
    bval = 1

def a_off():
    global rval, gval, bval, R,G,B
    rval = 0
    gval = 0
    bval = 0

def mkT (time_a,a = 1,b = 1):#주기, 비율로 받기
    time_a2 = time_a * (a / (a + b))
    time_a3 = time_a * (b / (a + b))
    while True:
        a_on()
        sleep(time_a2)
        a_off()
        sleep(time_a3)

def mkF (time_a,a,b):#주파수, 비율로 받기
    time_a2=1/time_a
    mkT(time_a2,a,b)


mkT(1,1,1)