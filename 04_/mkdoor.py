from gpiozero import LED,Button, AngularServo
from time import sleep
from signal import pause

G = LED(17)
R = LED(27)
btn1 = Button(14)
btn2 = Button(15)
servo = AngularServo(13,min_angle = 0, max_angle = 90)

pwd=[1,1,1,1,1]
ml=[]
a=-1
def suc():
    G.on()
    servo.angle=90
    sleep(1)
    servo.angle = 0
    sleep(1)

    G.off()
    print("success!")

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


def btn_1():
    global a, ml
    a += 1

    print(a+1,": 1 in")

    if a==3:
        openit()

        a=-1
        ml=[]
    else:
        ml.append(1)

def btn_0():

    global a, ml
    a += 1
    print(a+1, ": 0 in")

    if a==3:
        openit()

        a=-1
        ml=[]
    else:
        ml.append(0)


btn1.when_pressed = btn_1
btn2.when_pressed = btn_0

pause()