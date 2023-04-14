#LED2개와 레이저 모두 3초간 blink
from gpiozero import LED, Button
from time import sleep
from signal import pause

btn = Button(2)
b = LED(14)
r = LED(15)
l = LED(18)
t_flag = False

tem_num = 0
num_term = 1 # 손이 느려서 0.1은 테스트 못 할 것 같아 높였습니다

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
            for i in range(1,10):
                a_on(0.3)
                a_off(0.3)
        else:
            print("you lose, time : ",tem_num)
    return suc

while True:
    if t_flag :
        break
    tem_num = 0
    sleep(0.5)
    #for i in range(0, 90):
    while tem_num<=9:
        print(tem_num)
        if clk():
            t_flag = True
            break
        tem_num += num_term
        sleep(num_term)
    sleep(0.5)

    if t_flag :
        break
    #for i in range(1, 89, -1):
    while tem_num >= 0:
        tem_num -= num_term
        print(tem_num)
        if clk():
            t_flag = True
            break
        sleep(num_term)
print("success!")


