#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs import UInt16

class automaticWasteSegregator():
	def __init__(self):

		rospy.init_node('Primary_Program', anonymous=True)

		# state is 0 before start
		# state is changed to 1 if metal
		# state is changed to 2 if humid
		# state is changed to 3 if transparent
		# state is changed to 4 if shiny
		# state is changed to 5 if dense
		# else state is set to 6
		self.state = 0

		self.metal_sub = rospy.Subscriber('metal' , UInt16 , self.metal_callback)
		self.humid_sub = rospy.Subscriber('humidity' , UInt16 , self.humid_callback)
		self.ldr_sub = rospy.Subscriber('ldr' , UInt16 , self.ldr_callback)

		self.classify()

	def classify(self):
		rate = rospy.Rate(20)
		while not rospy.is_shutdown():
			if 

if __name__ == '__main__':
	print('Automatic Waste Segregator.\n\nVersion : 1.0.0')
	automaticWasteSegregator()
