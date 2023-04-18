from gpiozero import PWMLED,Button
from time import sleep

motor = PWMLED(14)
btn1 = Button(15)
btn2 = Button(18)
a=1
def movnslp(a,b) :
    motor.value=a
    print('speed =',a)
    sleep(b)

def a_go():
    global a
    if(a>3):
       a=1
    else:
        a+=1

def a_bo():
    global a
    if(a<1):
       a=3
    else:
        a-=1


while True:
    btn1.when_pressed = a_go
    btn2.when_pressed = a_bo
    movnslp(a,1)