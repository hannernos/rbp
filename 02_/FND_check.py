#FND test
from gpiozero import LED
from time import sleep

a = LED(14)
b = LED(26)
c = LED(15)
d = LED(18)
e = LED(23)
f = LED(24)
g =LED(25)
h = LED(8)

lst = [a,b,c,d,e,f,g,h]

for i in lst:
    lst[i].on()
