#!/usr/bin/env python3
#encoding:utf-8

from ev3dev.ev3 import *

# Put yer' calibrations here

class color:
	'''Reads value from color sensors'''
	# Can implement "tell me which side the green square is on" functionality

	def __init__(self,port):
		self.port = port # May not be needed
		self.colors = ('unknown','black','blue','green','yellow','red','white','brown')
		self.cl = ColorSensor(port) # Testing if objects will survive after initization of class
		self.cl.mode='COL-COLOR'
		assert self.cl.connected, "Connect a color sensor to port " + port #May not work

		print('initialized color sensor')

	def decodeColor(self):
		return self.colors[self.cl.value()]

	def decodeRawColor(self):
		self.cl.mode='RGB-RAW'
		red = self.cl.value(0)
		green = self.cl.value(1)
		blue = self.cl.value(2)

		return "Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue)


class infrared:
	''' Senses proximity of objects using infrared sensor'''
	def __init__(self,port):
		self.port = port

		self.ir = InfraredSensor()
		assert self.ir.connected, "Connect an infrared sensor to port " + port #May not work
		self.ir.mode = 'IR-PROX'

	def returnDistance(self):
		return self.ir.value()
