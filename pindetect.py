import RPi.GPIO as gpio
from subprocess import call
import time
import led
gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.IN, pull_up_down = gpio.PUD_UP)

def get_input(channel):
    print("Button Pushed")
    led.run_led(5)

gpio.add_event_detect(5, gpio.FALLING, callback=get_input, bouncetime=300)

while 1:
    time.sleep(360)
