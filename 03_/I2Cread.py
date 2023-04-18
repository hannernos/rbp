import smbus
from time import sleep
DEVICE_BUS = 1
DEVICE_ADDR = 0x76
bus = smbus.SMBus(DEVICE_BUS)

while True:
    a= bus.read_byte_data(DEVICE_ADDR, 0x00)
    print(a)
    sleep(1)