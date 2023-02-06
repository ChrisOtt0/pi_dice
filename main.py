import RPi as GPIO
import time

GPIO.setmode(GPIO.BCM)

def roll_dice():
    print("You pressed the button")
    GPIO.output(26, True)
    time.sleep(1)
    GPIO.output(26, False)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback = roll_dice)

i = 0
while True:
    i += 1
    print(i)
    time.sleep(1)
