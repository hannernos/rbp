from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

while True:
    humid = sense.get_humidity()
    temp = sense.get_temperature()
    press = sense.get_pressure()

    print("Humidith : %s" % humid)
    print("Temperature : %s" %temp)
    print('Pressure:%s'%press)
    sleep(1)