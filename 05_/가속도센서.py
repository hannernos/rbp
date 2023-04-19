from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    acc = sense.get_accelerometer_raw()
    print("가속도")
    print(f'[{acc["x"]:5.1f}] - ',end = '')
    print(f'[{acc["y"]:5.1f}] - ',end = '')
    print(f'[{acc["z"]:5.1f}] - ',end = '')
    print()

    print("자기력")
    com = sense.get_compass_raw()
    print(f'[{com["x"]:5.1f}] - ',end = '')
    print(f'[{com["y"]:5.1f}] - ',end = '')
    print(f'[{com["z"]:5.1f}] - ',end = '')
    print()