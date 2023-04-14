from gpiozero import LED
from time import sleep

b = LED(14)
r = LED(15)
g = LED(18)

bFlag=False
rFlag=False
gFlag=False

def a_on(i=1):
    b.on()
    r.on()
    g.on()
    sleep(i)
    
def a_off(i=30):
    b.off()
    r.off()
    g.off()
    sleep(i)
    
while True:
    #a_on()
    #a_off(30)
    in_i=int(input())
    if(in_i==1):
        if bFlag:
            bFlag=False
            b.off()
        else:
            bFlag=True
            b.on()
    elif(in_i==2):
        if rFlag:
            rFlag=False
            r.off()
        else:
            rFlag=True
            r.on()
    elif(in_i==3):
        if gFlag:
            gFlag=False
            g.off()
        else:
            gFlag=True
            g.on()
    
    
    
    
    