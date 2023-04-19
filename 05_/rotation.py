from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

sense.show_message("A")
sense.set_rotation(90)
sense.show_message("A")
sense.set_rotation(180)
sense.show_message("A")
sense.set_rotation(270)
sense.show_message("A")