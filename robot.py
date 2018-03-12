#!/usr/bin/env python3
#encoding:utf-8

#import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time import sleep
from lib import *

def main():
	i = 0 # Needed for incremental functions
	speed = 100 # Needed to set speed for algorithm test and D&R test

	# Declare your color ranges like this:
	black = (
		(0,0,0), # Lower RGB
		(60,65,54) # Upper RGB
	)
	green = (
		(0,195,0), # Lower RGB
		(100,1023,130) # Upper RGB
	)
	white = (
		(240,310,180), # Lower RGB
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

	# New Line following algorithm test
	print("Starting Line Algorithm test...")
	degrees = 800
	motor.runForever(speed=speed)

	print(str(i)+": Started")
	try:
		while True:
			i += 1
			print("\n"+str(i)+": cL "+colorL.decodeColor()+"\t cR: "+colorR.decodeColor())

			# Go Straight
			if colorL.decodeColorRange(black) and colorR.decodeColorRange(white):
				print(str(i)+": Straight")
				motor.runForever(speed=speed)
				i+=1

			# Line following (left bend)
			elif colorL.decodeColorRange(black) and colorR.decodeColor(white):
				#motor.stop() # Stop motor before turning
				print(str(i)+": left bend")
				motor.leftMotor(speed=speed*0.25)

				i += 1

			# Line following (right bend)
			elif colorR.decodeColorRange(black) and colorL.decodeColor(white):
				#motor.stop() # Stop motor before turning
				print(str(i)+": right bend")
				motor.rightMotor(speed=speed*0.25)

				i += 1

			# Check for endzone
			elif colorL.decodeColor() == 'green' and colorR.decodeColor() == 'green':
				print("endzone")

			#Check for bottle
			if infra.returnDistance() < '20':
				print("bottle")


			# Turn Left
			elif colorL.decodeColorRange(green) and colorR.decodeColorRange(white):
				motor.stop()  Stop motor before turning
				print(str(i)+": turned left")
				motor.leftMotor(speed=speed)
				motor.rightMotor(speed=-speed)

				sleep(1.5)
				motor.runForever(speed=speed)

				i += 1

			# Turn right
			elif colorR.decodeColorRange(green) and colorL.decodeColorRange(white):
				motor.stop()  Stop motor before turning
				print(str(i)+": turned right")
				motor.leftMotor(speed=-speed)
				motor.rightMotor(speed=speed)

				sleep(1.5)
				motor.runForever(speed=speed)

				i += 1

			# Do a 360 degree scan
			elif colorL.decodeColorRange(black) and colorR.decodeColorRange(black):
				print("Start scan")
				x = True
				while x == True:
					motor.stop()
					motor.leftMotor(speed=speed)
					motor.rightMotor(speed=-speed)

					if colorL.decodeColorRange(white) and colorR.decodeColorRange(white):
						print("End scan")
						x = False

	except KeyboardInterrupt:
		motor.stop()
		print("Finished Line Algorithm test v2 at "+str(i)+" steps.")
		i=0

	print("End of tests.")

	return 0


if __name__ == "__main__":
	main()
