#!/usr/bin/env python3
#encoding:utf-8

#import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time import sleep
from lib import *

def main():
	i = 0 # Needed for incremental functions
	speed = 100 # Needed to set speed for algorithm test and D&R test

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

	# New Line following algorithm test
	print("Starting Line Algorithm test v2...")
	degrees = 800
	motor.runForever(speed=speed)

	print(str(i)+": Started")
	try:
		while True:
			i += 1
			print("\n"+str(i)+": cL "+colorL.decodeColor()+"\t cR: "+colorR.decodeColor())

			# Go Straight
			if colorL.decodeColor() == 'white' or colorL.decodeColor() == 'black' and colorR.decodeColor() == 'white' or colorR.decodeColor() == 'black':
				print(str(i)+": Straight")
				motor.runForever(speed=speed)
				i+=1

			# Line following (left bend)
			elif colorL.decodeColor() == 'black' or colorL.decodeColor() == 'blue' and colorR.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				print(str(i)+": left bend")
				motor.leftMotor(speed=speed*0.25)

				i += 1

			# Line following (right bend)
			elif colorR.decodeColor() == 'black' or colorR.decodeColor() == 'blue' and colorL.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				print(str(i)+": right bend")
				motor.rightMotor(speed=speed*0.25)

				i += 1

			# Check for endzone
			elif colorL.decodeColor() == 'green' and colorR.decodeColor() == 'green':
				print("endzone")

			#Check for bottle
			elif infra.returnDistance() < '20':
				print("bottle")
				break


			# Turn Left
			#if colorL.decodeColor() == 'green' or colorL.decodeColor() == 'blue' and colorR.decodeColor() == 'white':
			#	motor.stop() # Stop motor before turning
			#	print(str(i)+": turned left")
			#	motor.leftMotor(speed=speed)
			#	motor.rightMotor(speed=-speed)

			#	sleep(1.5)
			#	motor.runForever(speed=speed)

			#	i += 1

			# Turn right
			#if colorR.decodeColor() == 'green' or colorR.decodeColor() == 'blue' and colorL.decodeColor() == 'white':
			#	motor.stop() # Stop motor before turning
			#	print(str(i)+": turned right")
			#	motor.leftMotor(speed=-speed)
			#	motor.rightMotor(speed=speed)

			#	sleep(1.5)
			#	motor.runForever(speed=speed)

			#	i += 1

			# Do a 360 degree scan
			#if colorL.decodeColor() == 'black' and colorR.decodeColor() == 'black':
			#	print("Start scan")
			#	x = True
			#	while x == True:
			#		motor.stop()
			#		motor.leftMotor(speed=speed)
			#		motor.rightMotor(speed=-speed)

			#		if colorL.decodeColor() == 'white' and colorR.decodeColor() == 'white':
			#			print("End scan")
			#			x = False

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
		(50,50,50) # Upper RGB
	)
	green = (
		(20,100,20), # Lower RGB
		(100,255,100) # Upper RGB
	)
	white = (
		(200,200,200), # Lower RGB
		(255,255,255) # Upper RGB
	)

	try:
		while True:
			# Black
			print(i+":")
			if colorL.decodeColorRange(black) == True: # How to use the method
				print("\tLeft sensor: black")
			if colorR.decodeColorRange(black) == True:
				print("\tRight sensor: black\n")
			sleep(0.05)

			# Green
			print(i+":")
			if colorL.decodeColorRange(green) == True:
				print("\tLeft sensor: green")
			if colorR.decodeColorRange(green) == True:
				print("\tRight sensor: green\n")
			sleep(0.05)

			# White
			print(i+":")
			if colorL.decodeColorRange(white) == True:
				print("\tLeft sensor: white")
			if colorR.decodeColorRange(white) == True:
				print("\tRight sensor: white\n")
			sleep(0.05)

			i+=1
	except KeyboardInterrupt:
		i = 0
		print("Ending color sensor test")

	return 0


if __name__ == "__main__":
	main()
