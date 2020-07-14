import RPi.GPIO as GPIO
import reports as reps
import time as ts
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10,GPIO.IN)
for x in range(10):
	GPIO.output(8,GPIO.HIGH)
	ts.sleep(0.1)
	reps.rep("gpio.in(10)", GPIO.input(10))
	ts.sleep(0.1)
	GPIO.output(8,GPIO.LOW)
	ts.sleep(0.1)
	reps.rep("gpio.in(10)", GPIO.input(10))
	ts.sleep(0.1)