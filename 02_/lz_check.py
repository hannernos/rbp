#LED2개와 레이저 모두 3초간 blink
from gpiozero import LED, Button
from time import sleep
from signal import pause

btn = Button(2)
b = LED(14)
r = LED(15)
l = LED(18)
bFlag = False
rFlag = False

tem_num = 0
num_term = 0.5 # 손이 느려서 0.1은 테스트 못 할 것 같아 0.5로 하였습니다

def a_on(i=1):
    b.on()
    r.on()
    l.on()
    sleep(i)


def a_off(i=30):
    b.off()
    r.off()
    l.off()
    sleep(i)
def clk():
    global tem_num
    suc = False
    if btn.is_pressed:
        if tem_num == 7:
            #3초간 깜빡
            suc = True
        else:
            print("you lose, time : ",tem_num)
    return suc

a_on()
sleep(10)



