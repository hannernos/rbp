from sense_hat import SenseHat
from time import sleep
#에뮬레이터로 할 떄는 sense_emu
#실제 sense hat으로 할 때는 sense_hat
sense = SenseHat()

X = [255,0,0] #red
O = [255,255,255] #white

map=[
    X, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
]

sense.set_pixels(map)
sleep(1)
sense.clear()#끄기