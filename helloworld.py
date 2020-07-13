import RPi.GPIO as GPIO
import reports as reps
import time as ts
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10,GPIO.IN)
i = 5
for x in range(5):
	reps.rep("gpio.in", GPIO.input(10))
	GPIO.output(8,GPIO.HIGH)
	ts.sleep(1)
	GPIO.output(8,GPIO.LOW)
	ts.sleep(1)

