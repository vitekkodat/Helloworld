import RPi.GPIO as GPIO
import reports as reps
import time as ts
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10,GPIO.IN)
reps.nrep()
for x in range(5):	
	GPIO.output(8,GPIO.HIGH)
	ts.sleep(0.5)
	reps.rep("gpio.in(10)", GPIO.input(10))
	ts.sleep(0.5)
	GPIO.output(8,GPIO.LOW)
	ts.sleep(0.5)
	reps.rep("gpio.in(10)", GPIO.input(10))
	ts.sleep(0.5)

