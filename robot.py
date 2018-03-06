#!/usr/bin/python3
#encoding:utf-8

#import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time import sleep
from lib import *

def main():
	i = 0 # Needed for incremental functions
	speed = 300 # Needed to set speed for algorithm test and D&R test

	# For fun
	name = "T-800"
	banner = '''[0;1;34;94m▀▛▘[0m  [0;1;34;94m▞▀▖▞▀▖▞▀▖[0m
	 [0;1;34;94m▌▄▄▖▚▄▘[0;34m▌▞▌▌▞▌[0m
	 [0;34m▌[0m   [0;34m▌[0m [0;34m▌▛[0m [0;34m▌▛[0m [0;34m▌[0m
	 [0;34m▘[0m   [0;34m▝▀[0m [0;37m▝▀[0m [0;37m▝▀[0m'''

	# Should implement so that when you load the program, it waits for a button
	# press to start moving. That way when starting the robot for the
	# competition, you don't have to wait for the program to be loaded, as you
	# should have already done that before.

	# Declare your objects here:
	btn = Button()
	motor = largeMotor(leftM='outA',rightM='outD')
	gripperM = tachoMotor(port='outB')
	colorL = color('in1') # This sensor needs to be on the left for the turning test
	colorR = color('in4') # This sensor needs to be on the right for the turning test
	infraredS = infrared('in2')

	# say our name (sorry, no forced memes here)
	print("Introducing the T-800 from Cyberdyne Systems")
	Sound.speak("Introducing the T-800, from Cyberdyne Systems. Programmed by Skynet.")
	print("Press any button to start")

	while btn.any()==False: # While no button is pressed.
		sleep(0.01)  # Wait 0.01 second

	# Gripper test
	print("Testing tacho motors...")
	gripperM.grip(position=100,speed=100)
	print("Ending tacho motor test")

	# Line following algorithm test
	print("Starting Line Algorithm test...")
	degrees = 800
	motor.runForever(speed=speed)

	print(str(i)+": Started")
	try:
		while True:
			sleep(0.5)
			i += 1
			print("\n"+str(i)+": "+colorL.decodeColor())
			print(str(i)+": Straight")

			# Turn Left
			if colorL.decodeColor() == 'blue' and colorR.decodeColor() == 'white':
				motor.stop() # Stop motor before turning
				motor.leftMotor(speed=speed)
				motor.rightMotor(speed=-speed)

				sleep(2)
				motor.runForever(speed=speed)

				i += 1
				print(str(i)+": turned left")

			# Turn right
			if colorR.decodeColor() == 'blue' and colorL.decodeColor() == 'white':
				motor.stop() # Stop motor before turning
				motor.leftMotor(speed=-speed)
				motor.rightMotor(speed=speed)

				sleep(2)
				motor.runForever(speed=speed)

				i += 1
				print(str(i)+": turned right")

			# Line following (left bend)
			if colorL.decodeColor() == 'black' and colorR.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				motor.leftMotor(speed=speed/2)
				motor.rightMotor(speed=speed)

				sleep(0.2)
				motor.stop()

				i += 1
				print(str(i)+": left bend")

			# Line following (right bend)
			if colorR.decodeColor() == 'black' and colorL.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				motor.leftMotor(speed=speed)
				motor.rightMotor(speed=speed/2)

				sleep(0.2)
				motor.stop()

				i += 1
				print(str(i)+": right bend")

			# Do a 360 degree scan
			if colorL.decodeColor() == 'black' and colorR.decodeColor() == 'black':
				x = True
				while x == True:
					motor.stop()
					motor.leftMotor(speed=speed)
					motor.rightMotor(speed=-speed)

					if colorL.decodeColor() == 'white' and colorR.decodeColor() == 'white':
						x = False

	except KeyboardInterrupt:
		motor.stop()
		print("Finished Line Algorithm test at "+str(i)+" steps.")
		i=0

	# New Line following algorithm test
	print("Starting Line Algorithm test v2...")
	degrees = 800
	motor.runForever(speed=speed)

	print(str(i)+": Started")
	try:
		while True:
			sleep(0.5)
			i += 1
			print("\n"+str(i)+": "+colorL.decodeColor())
			print(str(i)+": Straight")

			# Go Straight
			if colorL.decodeColor() == 'blue' and colorR.decodeColor() == 'blue':
				motor.runForever(speed=speed)
				i+=1

			# Turn Left
			if colorL.decodeColor() == 'blue' and colorR.decodeColor() == 'white':
				motor.stop() # Stop motor before turning
				motor.leftMotor(speed=speed)
				motor.rightMotor(speed=-speed)

				sleep(2)
				motor.runForever(speed=speed)

				i += 1
				print(str(i)+": turned left")

			# Turn right
			if colorR.decodeColor() == 'blue' and colorL.decodeColor() == 'white':
				motor.stop() # Stop motor before turning
				motor.leftMotor(speed=-speed)
				motor.rightMotor(speed=speed)

				sleep(2)
				motor.runForever(speed=speed)

				i += 1
				print(str(i)+": turned right")

			# Line following (left bend)
			if colorL.decodeColor() == 'black' and colorR.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				motor.rightMotor(speed=speed*1.75)

				i += 1
				print(str(i)+": left bend")

			# Line following (right bend)
			if colorR.decodeColor() == 'black' and colorL.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				motor.leftMotor(speed=speed*1.75)

				i += 1
				print(str(i)+": right bend")

			# Do a 360 degree scan
			if colorL.decodeColor() == 'black' and colorR.decodeColor() == 'black':
				x = True
				while x == True:
					motor.stop()
					motor.leftMotor(speed=speed)
					motor.rightMotor(speed=-speed)

					if colorL.decodeColor() == 'white' and colorR.decodeColor() == 'white':
						x = False

	except KeyboardInterrupt:
		motor.stop()
		print("Finished Line Algorithm test v2 at "+str(i)+" steps.")
		i=0

	# Infrared sensor test
	print("Starting infrared test...")
	try:
		while True:
			dist = infraredS.returnDistance()
			print(dist)
			sleep(1)
			i += 1
	except KeyboardInterrupt:
		i = 0
		print("Ending infrared test")

	# Color sensor test
	print("Starting color sensor test...")
	try:
		while True:
			print(colorL.decodeColor())
			sleep(1)
	except KeyboardInterrupt:
		print("Ending color sensor test")

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

	#cl = ColorSensor()
	#assert cl.connected, "Connect a sensor to any port"

	#cl.mode='COL-COLOR'
	#colors=('unknown','black','blue','green','yellow','red','white','brown')
	#while True:
	#	print(colors[cl.value()])
	#	#Sound.speak(colors[cl.value()]).wait()
	#	sleep(1)
	#Sound.beep()

	return 0


if __name__ == "__main__":
	main()
