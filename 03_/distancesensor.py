from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(21,20)

while True:
    print(sensor.distance, "m")
    sleep(0.1)