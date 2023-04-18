from signal import pause
from gpiozero import RotaryEncoder,Button

rotor = RotaryEncoder(16,20,wrap = True, max_steps=180)
rotor.steps=-180
rot_btn=Button(12)

def change_hue():
    print(rotor.steps)
def say_hello():
    print("hello")

rotor.when_rotated=change_hue()
rot_btn.whem_pressed = say_hello
pause()