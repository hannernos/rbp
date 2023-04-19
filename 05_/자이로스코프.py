from sense_hat import SenseHat
from time import sleep

sense = SenseHat()



def sdf():
    ori = sense.get_orientation_degrees()
    print(ori["yaw"])

while True:
    ori = sense.get_orientation_degrees()
    p=ori["pitch"]
    r=ori["roll"]
    print(p,r)