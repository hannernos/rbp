from gpiozero import LED
from time import sleep

blue = LED(17)

while True:
    blue.on()
    sleep(1)
    blue.off(1)
    sleep(30)

    for i in range(1, 100):
        blue.on()
        sleep(1/i)
        blue.off()
        sleep(1/i)