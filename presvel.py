import Adafruit_BBIO.ADC as ADC
from time import *

adcPin = "P9_36"

ADC.setup()

while(1)

	sleep(1)
	adcVal = ADC.read(adcPin)
	voltVal = adcVal*1.8
	actVoltVal = voltVal*(17000/7000)
	presVal = (((actVoltVal/5)-0.5)/0.2)*1000
	vel = abs(((2*presVal)/1.255))**0.5