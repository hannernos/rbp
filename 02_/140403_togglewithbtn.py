#toggle with button
from gpiozero import LED, Button
from time import sleep
from signal import pause

btn1 = Button(2)
btn2 = Button(3)
b = LED(14)
r = LED(15)
g = LED(18)

bFlag = False
rFlag = False
gFlag = False


def a_on(i=0):
    b.on()
    r.on()
    g.on()
    sleep(i)


def a_off(i=0):
    b.off()
    r.off()
    g.off()
    sleep(i)

def toggle_r(i=0):
    global rFlag
    if rFlag:
        rFlag = False
        r.off()
        sleep(i)
    else:
        rFlag = True
        r.on()
        sleep(i)
def toggle_g(i=0):
    global gFlag
    if gFlag:
        gFlag = False
        g.off()
        sleep(i)
    else:
        gFlag = True
        g.on()
        sleep(i)
def toggle_b(i=0):
    global bFlag
    if bFlag:
        bFlag = False
        r.off()
        sleep(i)
    else:
        bFlag = True
        r.on()
        sleep(i)


in_i = 1
while True:
    # a_on()
    # a_off(30)
    if btn1.is_pressed:
        toggle_r()


    if btn2.is_pressed:
        toggle_g()




