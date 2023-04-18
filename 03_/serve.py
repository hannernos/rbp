from gpiozero import AngularServo
from time import sleep
servo = AngularServo(21,min_angle = 0, max_alglr = 90)

servo.angle = 90