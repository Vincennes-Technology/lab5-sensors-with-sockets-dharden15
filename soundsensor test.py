#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD


lcd = LCD.Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BCM)


def setup():
    ADC.setup(0x48)

def loop():
    count = 0
    while True:
        voiceValue = ADC.read(0)
        if voiceValue:
            print 'Value:', voiceValue
            lcd.message("\n %s %%" % (voiceValue))
            if voiceValue < 100:
                print "Voice detected! ", count
                count += 1
                lcd.message("\n Voice detected!")
                time.sleep(0.5)

lcd.clear


if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		pass	


