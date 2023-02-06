import RPi.GPIO as GPIO
import random
import time

unit = 1
input_port = 18
outs = [22, 13, 26, 23, 12, 20]
GPIO.setmode(GPIO.BCM)

def blink():
    for p in outs:
        GPIO.output(p, False)

    ports = []
    for i in range(0, 6):
        x = random.randint(0, 1)
        if x == 1:
            ports.append(outs[i])

    for p in ports:
        GPIO.output(p, True)

    time.sleep(unit / 4)

    for p in ports:
        GPIO.output(p, False)
    

def roll_dice():
    for i in range(0, 6):
        blink()
        time.sleep(unit / 8)

    x = random.randint(1, 6)
    i = 0
    while i < x:
        GPIO.output(outs[i], True)
        i += 1

GPIO.setup(outs, GPIO.OUT)
GPIO.setup(input_port, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    pressed = GPIO.input(input_port)
    if not pressed:
        roll_dice()

GPIO.cleanup()
