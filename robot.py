#!/usr/bin/python3
#encoding:utf-8

#import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time import sleep
from lib import *

def main():
	i = 0 # Needed for incremental functions
	speed = 100 # Needed to set speed for algorithm test and D&R test

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
	colorL = color('in1') # This sensor needs to be on the left for the turning test
	colorR = color('in4') # This sensor needs to be on the right for the turning test
	

	# say our name (sorry, no forced memes here)
	print("Introducing the T-800 from Cyberdyne Systems")
	Sound.speak("Introducing the T-800, from Cyberdyne Systems. Programmed by Skynet.")
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
			print(str(i)+": Straight")

			# Go Straight
			if colorL.decodeColor() == 'white' or colorL.decodeColor() == 'black' and colorR.decodeColor() == 'white' or colorR.decodeColor() == 'black':
				motor.runForever(speed=speed)
				i+=1

			# Turn Left
			if colorL.decodeColor() == 'green' or colorL.decodeColor() == 'blue' and colorR.decodeColor() == 'white':
				motor.stop() # Stop motor before turning
				print(str(i)+": turned left")
				motor.leftMotor(speed=speed)
				motor.rightMotor(speed=-speed)

				sleep(1.5)
				motor.runForever(speed=speed)

				i += 1

			# Turn right
			if colorR.decodeColor() == 'green' or colorR.decodeColor() == 'blue' and colorL.decodeColor() == 'white':
				motor.stop() # Stop motor before turning
				print(str(i)+": turned right")
				motor.leftMotor(speed=-speed)
				motor.rightMotor(speed=speed)

				sleep(1.5)
				motor.runForever(speed=speed)

				i += 1

			# Line following (left bend)
			if colorL.decodeColor() == 'black' or colorL.decodeColor() == 'blue' and colorR.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				print(str(i)+": left bend")
				motor.leftMotor(speed=speed*0.25)

				i += 1

			# Line following (right bend)
			if colorR.decodeColor() == 'black' or colorR.decodeColor() == 'blue' and colorL.decodeColor() == 'white':
				#motor.stop() # Stop motor before turning
				print(str(i)+": right bend")
				motor.rightMotor(speed=speed*0.25)

				i += 1

			# Check for endzone
			if colorL.decodeColor() == 'green' and colorR.decodeColor() == 'green':
				print("endzone")
				
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
