#!/usr/bin/env python3
#encoding:utf-8

#import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time import sleep
from lib import *

def main():
	i = 0 # Needed for incremental functions
	speed = 100 # Needed to set speed for algorithm test and D&R test
	
	#Color range
	black = (
		(0,0,0), # lower RGB
		(60,65,54) # upper RGB
	)
	green = (
		(0,195,0),
		(190,1023,130)
	)
	white = (
		(360,310,180),
		(1023,1023,1023)
	)
	
	#For tower:
	rotate = 65/speed # For turning
	width = 300/speed # Used for going the width of the tower
	length =500/speed # Used for going the length of the tower
	towerDistance = 30 # Distance from tower
	turnSpeed = 2 # Used for turning around tower
	
	#For Endzone
	canDist = 40 
	canDistGrab = 2
	
	
	# Should implement so that when you load the program, it waits for a button
	# press to start moving. That way when starting the robot for the
	# competition, you don't have to wait for the program to be loaded, as you
	# should have already done that before.

	# Declare your objects here:
	btn = Button()
	motor = largeMotor(leftM='outA',rightM='outD')
	colorL = color('in1') # This sensor needs to be on the left for the turning test
	colorR = color('in4') # This sensor needs to be on the right for the turning test
	infra = infrared('in3')

	# say our name
	print("Press any button to start")

	while btn.any()==False: # While no button is pressed.
		sleep(0.01)  # Wait 0.01 second

	#New Line following algorithm test
	# print("Starting Line Algorithm test v2...")
	# degrees = 800
	# motor.runForever(speed=speed)

	print(str(i)+": Started")
	try:
			while True:
				i += 1

			#Check for bottle
				if infra.returnDistance() < towerDistance:
					motor.stop() #stop motor before turning
					print("bottle")
					
					#Rotate 90 degrees
					motor.rightMotor(speed=speed*2)
					motor.leftMotor(speed=speed*-2)
					sleep(rotate) #The time it waits is based on speed so that a changed speed does not increase the distance
					motor.stop()
					
					motor.runForever(speed=speed)
					sleep(width)
					motor.stop()
					
					motor.rightMotor(speed=speed*-2)
					motor.leftMotor(speed=speed*2)
					sleep(rotate)
					motor.stop()
					
					#Move past tower
					motor.runForever(speed=speed)
					sleep(length)
					motor.stop()
					
					motor.rightMotor(speed=speed*-2)
					motor.leftMotor(speed=speed*2)
					sleep(rotate) 
					motor.stop()
					
					motor.runForever(speed=speed)
					sleep(width)
					motor.stop()
					
					motor.rightMotor(speed=speed*2)
					motor.leftMotor(speed=speed*-2)
					sleep(rotate)
					motor.stop()
					

				elif colorL.decodeColorRange(green) and colorR.decodeColorRange(green):
					motor.stop()
					print("Endzone")
					
					while True:
						if infra.returnDistance() > canDist:
						
							print("Searching for can")
							motor.rightMotor(speed=speed*2)
							motor.leftMotor(speed=speed*-2)
					
					
						else:
							break
							
					print("Found can")
					while True:
						if infra.returnDistance() > canDistGrab:
							
					
					break
					
					
				# elif colorL.decodeColorRange(white) and colorR.decodeColorRange(white):
					# print("Runforever")
					# motor.runForever(speed=speed)
	
	
	
	except KeyboardInterrupt:
		motor.stop()
		print("Finished Line Algorithm test v2 at "+str(i)+" steps.")
		i=0

	print("Press any button on ev3 to continue")
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

	# Declare your color ranges like this:
	black = (
		(0,0,0), # Lower RGB
		(100,100,100) # Upper RGB
	)
	green = (
		(20,100,20), # Lower RGB
		(150,1023,170) # Upper RGB
	)
	white = (
		(200,200,160), # Lower RGB
		(1023,1023,1023) # Upper RGB (max value for color sensor is 1023)
	)

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

	return 0


if __name__ == "__main__":
	main()
