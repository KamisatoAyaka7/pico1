from machine import Pin
from time import sleep
from random import randint

led=Pin(25,Pin.OUT)
led.on()

s1=Pin(0,Pin.IN,Pin.PULL_UP)
s2=Pin(3,Pin.IN,Pin.PULL_UP)
s3=Pin(6,Pin.IN,Pin.PULL_UP)
s4=Pin(12,Pin.IN,Pin.PULL_UP)
s5=Pin(15,Pin.IN,Pin.PULL_UP)
ss=[s1,s2,s3,s4,s5]

l1=Pin(1,Pin.OUT)
l2=Pin(4,Pin.OUT)
l3=Pin(26,Pin.OUT)
l4=Pin(21,Pin.OUT)
l5=Pin(18,Pin.OUT)
ls=[l1,l2,l3,l4,l5]

lv1=Pin(5,Pin.OUT)
lv2=Pin(7,Pin.OUT)
lv3=Pin(8,Pin.OUT)
lv4=Pin(28,Pin.OUT)
lv5=Pin(27,Pin.OUT)
lvs=[lv1,lv2,lv3,lv4,lv5]

score=0
index=0
a=0
waittime=0
limwait=30000

def isPressed(obj):
    if obj.value()==0:
        sleep(0.01)
        if obj.value()==0:
            return True
    return False

def myinit():
    for i in range(5):
        ls[i].off()
        lvs[i].off()

def fail():
    for i in range(3):
        for l in ls:
            l.on()
        for lv in lvs:
            lv.on()
        sleep(0.5)
        for l in ls:
            l.off()
        for lv in lvs:
            lv.off()
        sleep(0.5)
    myinit()

myinit()
while True:
    p1=True
    p2=True
    waittime=0
    while a==index:
        a=randint(0,4)
    index=a
    ls[a].on()
    while p1:
        waittime+=1
        if waittime>limwait and score!=0:
            fail()
            score=0
            break
        for i in range(5):
            if isPressed(ss[i]):
                waittime=0
                if i==a and p2:
                    score+=1
                elif p2:
                    fail()
                    score=0
                p2=False
                while p1:
                    if not isPressed(ss[i]):
                        p1 = False
                        p2 = True
        sleep(0.01)
        
    if score<9:
        limwait=200
    if score>=9:
        lv1.on()
        limwait=200
    if score>=27:
        lv2.on()
        limwait=200
    if score>=108:
        lv3.on()
        limwait=200
    if score>=900:
        lv4.on()
        limwait=150
    if score>=3600:
        lv5.on()
        limwait=100     
    ls[a].off()
    