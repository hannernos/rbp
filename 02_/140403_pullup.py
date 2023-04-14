#풀다운 회로 테스트
from gpiozero import LED, Button
from time import sleep
from signal import pause

btn1 = Button(2)
btn2 = Button(3)
b = LED(14)
r = LED(15)
g = LED(18)

while True:
    # a_on()
    # a_off(30)
    if btn1.is_pressed:
        print("2")
        sleep(1)

    if btn2.is_pressed:
        print("3")
        sleep(1)



