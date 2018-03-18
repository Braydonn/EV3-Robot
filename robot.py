#!/usr/bin/env python3
#encoding:utf-8

#import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time import sleep
from lib import *

def main():
	i = 0 # Needed for incremental functions
	speed = 150 # Needed to set speed for algorithm test and D&R test
	position = 50

	# Declare your color ranges like this:
	black = (
		(0,0,0), # Lower RGB
		(60,65,54) # Upper RGB
	)
	green = (
		(0,190,0), # Lower RGB
		(168,1023,140) # Upper RGB
	)
	white = (
		(220,310,170), # Lower RGB
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
		
		# Raw color sensor test
	print("Starting color sensor test...")
	try:
		while True:
			print(str(i)+":")
			print("Left Color Sensor: "+colorL.decodeRawColor())
			print("Right Color Sensor: "+colorR.decodeRawColor()+'\n')

			i += 1
			sleep(1)
	except KeyboardInterrupt:
		i = 0
		print("Ending color sensor test")

	# Color Range detection demo and test
	print("Color Range Detection test starting...\n")

	try:
		while True:
			# Black
			print(str(i)+": Black")
			if colorL.decodeColorRange(black) == True: # How to use the method
				print("\tLeft sensor: black")
			if colorR.decodeColorRange(black) == True:
				print("\tRight sensor: black\n")
			sleep(2)
			print()

			# Green
			print(str(i)+": Green")
			if colorL.decodeColorRange(green) == True:
				print("\tLeft sensor: green")
			if colorR.decodeColorRange(green) == True:
				print("\tRight sensor: green\n")
			sleep(2)
			print()

			# White
			print(str(i)+": White")
			if colorL.decodeColorRange(white) == True:
				print("\tLeft sensor: white")
			if colorR.decodeColorRange(white) == True:
				print("\tRight sensor: white\n")
			sleep(2)

			print()

			i+=1
	except KeyboardInterrupt:
		i = 0
		print("Ending color sensor test")

	print("start line algorithm test")
	try:
		while True:			
			if colorL.decodeColorRange(black):
				motor.stop()
				motor.turnLeft(speed=speed,position=position)
			elif colorR.decodeColorRange(black):
				motor.stop()
				motor.turnRight(speed=speed,position=position)
			elif colorL.decodeColorRange(green):
				motor.stop()
				print("turn left!")
				motor.turnLeft(speed=speed,position=300)
				motor.runTimed(speed=speed,time=1000)
			elif colorR.decodeColorRange(green):
				motor.stop()
				print("turn right!")
				motor.turnRight(speed=speed,position=300)
				motor.runTimed(speed=speed,time=1000)
			else:
				motor.runForever(speed=speed)
	except KeyboardInterrupt:
		print("end line algorithm test")


	return 0


if __name__ == "__main__":
	main()
