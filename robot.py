#!/usr/bin/env python3
#encoding:utf-8

#import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time import sleep
from lib import *

def main():
	i = 0 # Needed for incremental functions
	speed = 150 # Needed to set speed for algorithm test and D&R test
	position = 60

	# Declare your color ranges like this:
	black = (
		(0,0,0), # Lower RGB
		(180,100,100) # Upper RGB
	)
	green = (
		(0,190,0), # Lower RGB
		(140,1023,140) # Upper RGB
	)
	white = (
		(210,300,160), # Lower RGB
		(1023,1023,1023) # Upper RGB (max value for color sensor is 1023)
	)

	# Declare your objects here:
	btn = Button()
	motor = largeMotor(leftM='outA',rightM='outD')
	colorL = color('in1') # This sensor needs to be on the left for the turning test
	colorR = color('in4') # This sensor needs to be on the right for the turning test
	infra = infrared('in3')

	print("Press any button to start")

	while btn.any()==False: # While no button is pressed.
		sleep(0.01)  # Wait 0.01 second
		

	# Color Range detection demo and test
	print("Color Range Detection test starting...\n")

	try:
		while True:
			# Straight
			if colorL.decodeColorRange(white,"white") and colorR.decodeColorRange(white,"white"):
				motor.runForever(speed=speed)
				print("Straight")

			# Right bend
			elif colorR.decodeColorRange(black,"black") and colorL.decodeColorRange(white,"white"):
				motor.turnRight(speed=speed,position=position)
				motor.runTimed(speed=speed,time=80)
				print("Right Bend")
			# Left bend
			elif colorL.decodeColorRange(black,"black") and colorR.decodeColorRange(white,"white"):
				motor.turnLeft(speed=speed,position=position)
				motor.runTimed(speed=speed,time=80)
				print("Left Bend")
			# Turning code
			#elif colorL.decodeColorRange(black) and colorR.decodeColorRange(black):
			#	motor.runTimed(speed=-speed,time=250)
				
			# Turn right
			elif colorR.decodeColorRange(green,"green"):
				motor.runTimed(speed=speed,time=200)
				motor.turnRight(speed=speed,position=152)
				motor.runTimed(speed=speed,time=100)
				#motor.runTimed(speed=speed,time=1000)
				print("Turn Right")
			# Else, turn left
			elif colorL.decodeColorRange(green,"green"):
				motor.runTimed(speed=speed,time=200)
				motor.turnLeft(speed=speed,position=152)
				motor.runTimed(speed=speed,time=100)
				#motor.runTimed(speed=speed,time=1000)
				print("Turn Left")
			else:
				motor.runForever(speed=speed)
	except KeyboardInterrupt:
		i = 0
		print("Ending color sensor test")

	motor.stop()

	return 0


if __name__ == "__main__":
	main()
