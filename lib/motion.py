#!/usr/bin/env python3
#encoding:utf-8
from ev3dev.ev3 import *

class largeMotor:
	'''Implements turning and drive functionality in an easy-to-use library. Needs two motors to work.'''

	def __init__(self,leftM,rightM):
		# Create motor objects
		self.leftM = LargeMotor(leftM)
		self.rightM = LargeMotor(rightM)

		print("initializing object")

	def runForever(self,speed):
		# Doesn't have wait_while block as you may need to run motor while
		# checking color sensors for example
		self.leftM.run_forever(speed_sp=-speed)
		self.rightM.run_forever(speed_sp=-speed)
		# Use stop() method to stop motors

	def runTimed(self,speed,time): # Change how time is handled by passing values to method?
		self.leftM.run_timed(time_sp=time,speed_sp=-speed,stop_action='brake')
		self.rightM.run_timed(time_sp=time,speed_sp=-speed,stop_action='brake')

		self.leftM.wait_while('running') # Stops program from running when motors are running


	# Turning methods
	def turnLeft(self,speed,position): # Turns left by activating right wheel
		self.rightM.run_to_rel_pos(position_sp=-position,speed_sp=speed,stop_action='hold')
		self.leftM.run_to_rel_pos(position_sp=position,speed_sp=speed,stop_action='hold')
		self.rightM.wait_while('running')

	def turnRight(self,speed,position): # Turns right by activating left wheel
		self.leftM.run_to_rel_pos(position_sp=-position,speed_sp=speed,stop_action='hold')
		self.rightM.run_to_rel_pos(position_sp=position,speed_sp=speed,stop_action='hold')
		self.rightM.wait_while('running')


	# Single motor control
	def leftMotor(self,speed):
		self.leftM.run_forever(speed_sp=-speed,stop_action='brake')

	def rightMotor(self,speed):
		self.rightM.run_forever(speed_sp=-speed,stop_action='brake')


	# Control methods
	def stop(self):
		self.leftM.stop(stop_action="brake")
		self.rightM.stop(stop_action="brake")

	def hold(self): # Will this work?
		self.leftM.wait_while('running')
		self.rightM.wait_while('running')

	def holdLeft(self):
		self.leftM.wait_while('running')

	def holdRight(self):
		self.leftM.wait_while('running')

class tachoMotor:
	'''For gripper'''
	def __init__(self,port):
		# Creating motor object:
		self.motor = Motor(port)

		print("initializing object")

	def grip(self,position,speed):
		self.motor.run_to_rel_pos(position_sp=position,speed_sp=speed,stop_action="hold")
		print("Gripping at "+str(position)+" with a speed of "+str(speed))
