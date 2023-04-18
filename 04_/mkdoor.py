from gpiozero import LED,Button, AngularServo
from time import sleep

R = LED(27)
G = LED(17)
btn1 = Button(14)
btn2 = Button(15)
servo = AngularServo(13,min_angle = 0, max_angle = 90)

pwd=[1,1,1,1]
ml=[]
a=0

def suc():
    G.on()
    servo.angle=90
    sleep(0.5)
    servo.angle = 0
    sleep(0.5)

    G.off()
    print("succecc!")

def fail():
    R.on()
    sleep(1)


    R.off()
    print("fail~")
def openit():
    mflag = 0
    for idx,i in enumerate (ml):
        if (i !=pwd[idx]):
            mflag=1
            break
    if (mflag == 1):
        fail()
    else:
        suc()

def btn0(b):
    global a, ml
    a+=1
    if a==4:
        openit()
        a=1
        ml=[b]
    else:
        ml.append(b)


btn1.when_pressed = btn0(1)
btn2.when_pressed = btn0(2)

while True:

    sleep(1)