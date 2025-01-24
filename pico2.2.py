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
index=[4,4,4,4]
time=0
limtime=0
press=True

def isClicked(obj):
    if obj.value()==0:
        sleep(0.01)
        if obj.value()==0:
            while obj.value()==0:
                sleep(0.01)
            return True
    return False

def myinit():
    for i in range(5):
        ls[i].off()
        lvs[i].off()
    global score
    score=0
    global index
    index=[4,4,4,4]
    global press
    press=True
    global limtime
    limtime=200
    global time
    time=0

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

def rand():
    global index
    while True:
        a=randint(0,4)
        for i in range(4):
            if index[i]!=a:
                index[3]=index[2]
                index[2]=index[1]
                index[1]=index[0]
                index[0]=a
                return a
            
def level6():
    for i in range(5):
        ls[i].on()
        lvs[i].on()
    sleep(10)
    myinit()
            
def levels():
    for i in range(5):
        lvs[i].off()
    if score>=9:
        lv1.on()
        limtime=200
    if score>=27:
        lv2.on()
        limtime=200
    if score>=108:
        lv3.on()
        limtime=200
    if score>=540:
        lv4.on()
        limtime=150
    if score>=3240:
        lv5.on()
        limtime=100
    if score>=20000:
        level6()

myinit()

while True:
    press=True
    ls[rand()].on()
    while press:
        time+=1
        if time>limtime and score!=0:
            time=0
            score-=1
            break
        for i in range(5):
            if isClicked(ss[i]):
                time=0
                times=0
                if i==index[0]:
                    score+=1
                else:
                    fail()
                press=False
        sleep(0.01)
    levels()
    ls[index[0]].off()
    