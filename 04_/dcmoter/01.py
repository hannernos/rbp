from gpiozero import PWMLED
from time import sleep

motor = PWMLED(3)

def movnslp(a,b) :
    motor.value=a
    print('speed =',a)
    sleep(b)


while True:
    movnslp(0,1)
    movnslp(1,2)
    movnslp(3,2)
    movnslp(5,2)