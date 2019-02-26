import I2C_LCD_driver
from time import *
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

servoPin = "P9_14"
down = "P9_23"
up = "P9_30"

GPIO.setup(up,GPIO.IN)
GPIO.setup(down,GPIO.IN)

deg = 45
dutyCycle = float(4./90.*deg+4)
PWM.start(servoPin,dutyCycle,50)

def GPIO_up():

	global deg 
	deg = deg + 1
	dutyCycle = float(4./90.*deg+4)
	PWM.set_duty_cycle(servoPin,dutyCycle)
	return deg

def GPIO_down():

	global deg 
	deg = deg - 1
	dutyCycle = float(4./90.*deg+4)
	PWM.set_duty_cycle(servoPin,dutyCycle)
	return deg

try:
	while(1):
		if GPIO.input(up)
			GPIO_up()
			sleep(0.05)
		elif GPIO.input(down)
			GPIO_down()
			sleep(0.05)
finally:
		PWM.cleanup()

