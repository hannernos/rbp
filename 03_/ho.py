from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(2)

Ubtn = Button(16)
Dbtn = Button(20)
val = 5
def UP():
    global val
    val += 1
    if val > 9:
        val = 9

def DOWN():
    global val
    val -= 1
    if val < 1:
        val = 1

Ubtn.when_pressed = UP
Dbtn.when_pressed = DOWN
while True:
    led.on()
    sleep( 0.0002 * val  ) #1~9
    led.off()
    sleep( 0.0002 * (10-val)  )

pause()