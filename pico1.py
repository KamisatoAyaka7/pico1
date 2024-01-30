from machine import Pin
from time import sleep
from random import randint

led=Pin(25,Pin.OUT)
led.on()

s1=Pin(15,Pin.IN,Pin.PULL_UP)
s2=Pin(13,Pin.IN,Pin.PULL_UP)
s3=Pin(10,Pin.IN,Pin.PULL_UP)
s4=Pin(8,Pin.IN,Pin.PULL_UP)
s5=Pin(4,Pin.IN,Pin.PULL_UP)
s6=Pin(3,Pin.IN,Pin.PULL_UP)
ss=[s1,s2,s3,s4,s5,s6]

l1=Pin(16,Pin.OUT)
l2=Pin(20,Pin.OUT)
l3=Pin(22,Pin.OUT)
l4=Pin(27,Pin.OUT)
l5=Pin(28,Pin.OUT)

ls=[l1,l2,l3,l4,l5]

while True:
    b=True
    a=randint(0,4)
    ls[a].toggle()
    while b:
        for i in range(0,5):
            if ss[i].value()==0:
                sleep(0.01)
                if ss[i].value()==0:
                    if i==a:
                        ls[i].toggle()
                        b=False
                    while ss[i].value()==0:
                        sleep(0.01)
