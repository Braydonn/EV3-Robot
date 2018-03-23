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
		(190,1023,140)
	)
	white = (
		(360,310,180),
		(1023,1023,1023)
	)
	
	#For watertower:
	wtRotate = 65/speed # For turning
	wtWidth = 300/speed # Used for going the width of the tower
	wtLength =500/speed # Used for going the length of the tower
	wtDist = 30 # Distance from tower
	wtTurnSpeed = speed*2 # Used for turning around tower
	
	#For Endzone:
	canDist = 40
	canGrabDist = 4
	
	platformDist = 30
	platormPlaceDist = 4
	
	# Should implement so that when you load the program, it waits for a button
	# press to start moving. That way when starting the robot for the
	# competition, you don't have to wait for the program to be loaded, as you
	# should have already done that before.

	# Declare your objects here:
	btn = Button()
	motor = largeMotor(leftM='outA',rightM='outD')
	tacho = tachoMotor(leftM='outB',rightM='outC')
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

	# tacho.grip(position=-500,speed=200) # Negative position pulls can down
	# tacho.stop()
	
	print(str(i)+": Started")
	try:
			while True:
				i += 1

				#Check for bottle
				if infra.returnDistance() < wtDist:
					motor.stop() #stop motor before turning
					print("bottle")
					
					#Rotate
					motor.rightMotor(speed=wtTurnSpeed)
					motor.leftMotor(speed=-wtTurnSpeed)
					sleep(wtRotate) #The time it waits is based on speed so that a changed speed does not increase the distance
					motor.stop()
					
					motor.runForever(speed=speed)
					sleep(wtWidth)
					motor.stop()
					
					motor.rightMotor(speed=-wtTurnSpeed)
					motor.leftMotor(speed=wtTurnSpeed)
					sleep(wtRotate)
					motor.stop()
					
					#Move past tower
					motor.runForever(speed=speed)
					sleep(wtLength)
					motor.stop()
					
					#Rotate
					motor.rightMotor(speed=-wtTurnSpeed)
					motor.leftMotor(speed=wtTurnSpeed)
					sleep(wtRotate) 
					motor.stop()
					
					motor.runForever(speed=speed)
					sleep(wtWidth)
					motor.stop()
					
					motor.rightMotor(speed=wtTurnSpeed)
					motor.leftMotor(speed=-wtTurnSpeed)
					sleep(wtRotate)
					motor.stop()
					
				#Test for endzone
				elif colorL.decodeColorRange(green) and colorR.decodeColorRange(green):
					motor.stop()
					print("Endzone")
					
					#Search for can
					motor.rightMotor(speed=speed*2)
					motor.leftMotor(speed=speed*-2)
					while True:	
						if infra.returnDistance() < canDist:
							break
					
						else:
							print("Searching for can")
					
					sleep(10/speed)
					motor.stop()
					print("Found can")
					
					#Go to can
					motor.runForever(speed=speed)
					while True:
						if infra.returnDistance() < canGrabDist:
							break
						else:
							print("Going to can")
					sleep(15/speed)
					motor.stop()
					
					#Pickup can
					tacho.grip(position=180,speed=150)
					tacho.stop
					
					#Search for platform
					motor.rightMotor(speed=speed*2)
					motor.leftMotor(speed=speed*-2)
					while True:	
						if infra.returnDistance() < platformDist:
							break
					
						else:
							print("Searching for platform")
							
					sleep(10/speed)
					motor.stop()
					print("Found platform")
					
					#Go to platform
					motor.runForever(speed=speed)
					while True:
						if infra.returnDistance() < platormPlaceDist:
							break
						else:
							print("Going to platform")
					sleep(15/speed)
					motor.stop()
					
					#Put down can
					tacho.grip(position=180,speed=150)
					tacho.stop
					
					break
					
	except KeyboardInterrupt:
		motor.stop()
		print("end line algorithm test")
	
	return 0


if __name__ == "__main__":
	main()
