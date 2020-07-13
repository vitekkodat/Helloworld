import RPi.GPIO as GPIO
import reports as reps
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)
i = 5
for x in range(5):
	reps.rep("ahoj", i)
	GPIO.output(8,GPIO.HIGH)
	sleep(1)
	GPIO.output(8,GPIO.LOW)
	sleep(1)

