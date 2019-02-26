from updown import deg
import I2C_LCD_driver
from time import *
import Adafruit_BBIO.GPIO as GPIO
from presvel import *

swap = "P9_27"

GPIO.setup(swap,GPIO.IN)
lcd = I2C_LCD_driver.lcd()

angle = deg - 45

n = 0

def displayOne():
	lcd.lcd_display_string("Angle: {} \337   ".format(angle), 1)
	lcd.lcd_display_string("Vel: {} m/s   ".format(round(vel,1)),2)
	global n 
	n = 1

def displayTwo():
	lcd.lcd_display_string("dP: {} Pa    ".format(round(presVal),3),1)
	lcd.lcd_display_string("Vel: {} ft/s    ".format(round((vel/.305),1)),2)
	global n
	n = 0

while(1):

	if GPIO.input(swap)
		if n == 0:
			displayOne()
		else:
			displayTwo()

