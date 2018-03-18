#!/usr/bin/env python3
#encoding:utf-8

from ev3dev.ev3 import *

class color:
	'''Reads value from color sensors'''
	# Can implement "tell me which side the green square is on" functionality

	def __init__(self,port):
		self.port = port
		self.colors = ('unknown','black','blue','green','yellow','red','white','brown')
		self.cl = ColorSensor(port)
		self.cl.mode='COL-COLOR'
		assert self.cl.connected, "Connect a color sensor to port " + port

		print('initialized color sensor')

	def decodeColor(self):
		self.cl.mode='COL-COLOR'
		return self.colors[self.cl.value()]

	# New and improved way of colour detection
	def decodeColorRange(self,color):
		# Set mode of color sensor
		self.cl.mode='RGB-RAW'
		
		# Red checking block
		if color[0][0] < self.cl.value(0) and color[1][0] > self.cl.value(0): # Lower red value
			print("Passed red") # For debugging
		else:
			red = self.cl.value(0)
			print("Failed red: "+str(red))
			return False

		# Green checking block
		if color[0][1] < self.cl.value(1) and color[1][1] > self.cl.value(1): # Lower green value
			print("Passed green")
		else:
			green = self.cl.value(1)
			print("Failed green: "+str(green))
			return False

		# Blue checking block
		if color[0][2] < self.cl.value(2) and color[1][2] > self.cl.value(2): # Lower blue value
			print("Passed blue")
			return True # Passed all tests, color sensed is x color
		else:
			blue = self.cl.value(2)
			print("Failed blue: "+str(blue)+'\n\n')
			return False


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
