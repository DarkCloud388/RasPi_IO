import RPi.GPIO as GPIO
import time
def run_led(lightTime):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)
	print "LED on"
	GPIO.output(18,GPIO.HIGH)
	time.sleep(lightTime)
	print "LED off"
	GPIO.output(18,GPIO.LOW)
run_led(1)
