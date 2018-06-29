#!/usr/bin/env python

import roslib
import rospy
from sensor_msgs.msg import BatteryState
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from geometry_msgs.msg import Twist, PointStamped
from actionlib_msgs.msg import *
import os

class BatteryManagement():
	def __init__(self):
		#rate = rospy.Rate(10)
		rospy.init_node('batterystuff', anonymous = False)
		self.home_pub = rospy.Publisher('/clicked_point', PointStamped, queue_size = 10)
 
		rospy.Subscriber('battery_state', BatteryState, self.callback)
		rospy.spin()

		# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")
		# What function to call when you ctrl + c    
		rospy.on_shutdown(self.shutdown)

	#Processing BatteryState data from init
	def callback(self, data):
		rospy.loginfo("Battery Voltage: %10.4f", (data.voltage))
		#rospy.loginfo("Battery Charge: %f", (data.charge))
		#rospy.loginfo("Battery percentage: %f", (data.percentage))
		#rospy.loginfo("Battery capacity: %10.4f", (data.capacity))
		rospy.loginfo("design capacity: %f", (data.design_capacity))

		#low battery threshold = 11.00 
		if (data.voltage > 11.00):

			# os.system('killall -9 rosmaster')
			self.gohome()


	# Move to origin point if voltage > 11.00
	# This will eventually move the robot home if voltage <= 11.00,
	# when battery is low	
	def gohome(self):
		#How often should we tell it to move? 10 HZ
		rate = rospy.Rate(10)
		homepoly1 = PointStamped()	#Corners of polygon
		homepoly2 = PointStamped()
		homepoly3 = PointStamped()
		homepoly4 = PointStamped()
		homepoly5 = PointStamped()
		homepoint = PointStamped()	#Origin point

		homepoly1.point.x = 0.001
		homepoly1.point.y = -0.001
		homepoly1.point.z = 0.0
		homepoly1.header.frame_id = "map"
		homepoly1.header.seq = 0
		homepoly1.header.stamp = rospy.Time.now()

		homepoly2.point.x = -0.001
		homepoly2.point.y = -0.001
		homepoly2.point.z = 0.0
		homepoly2.header.frame_id = "map"
		homepoly2.header.seq = 1
		homepoly2.header.stamp = rospy.Time.now()

		homepoly3.point.x = -0.001
		homepoly3.point.y = 0.001
		homepoly3.point.z = 0.0
		homepoly3.header.frame_id = "map"
		homepoly3.header.seq = 2
		homepoly3.header.stamp = rospy.Time.now()

		homepoly4.point.x = 0.001
		homepoly4.point.y = 0.001
		homepoly4.point.z = 0.0
		homepoly4.header.frame_id = "map"
		homepoly4.header.seq = 3
		homepoly4.header.stamp = rospy.Time.now()

		homepoly5.point.x = 0.001
		homepoly5.point.y = -0.001
		homepoly5.point.z = 0.0
		homepoly5.header.frame_id = "map"
		homepoly5.header.seq = 4
		homepoly5.header.stamp = rospy.Time.now()

		homepoint.point.x = 0.0
		homepoint.point.y = 0.0
		homepoint.point.z = 0.0
		homepoint.header.frame_id = "map"
		homepoint.header.seq = 5
		homepoint.header.stamp = rospy.Time.now()

		rospy.loginfo(homepoly1)
		self.home_pub.publish(homepoly1)
		rate.sleep()

		rospy.loginfo(homepoly2)
		self.home_pub.publish(homepoly2)
		rate.sleep()

		rospy.loginfo(homepoly3)
		self.home_pub.publish(homepoly3)
		rate.sleep()

		rospy.loginfo(homepoly4)
		self.home_pub.publish(homepoly4)
		rate.sleep()

		rospy.loginfo(homepoly5)
		self.home_pub.publish(homepoly5)
		rate.sleep()

		rospy.loginfo(homepoint)
		self.home_pub.publish(homepoint)
		rate.sleep()

		print("reached")

		# # Twist is a datatype for velocity
		# move_cmd = Twist()
		# # go forward at 0.2 m/s
		# move_cmd.linear.x = 0.2
		# # turn at 0 radians/self
		# move_cmd.angular.z = 0

		# # as long as you haven't ctrl + c keeping doing...
		# 	# publish the velocity
		# self.cmd_vel.publish(move_cmd)

	# stop turtlebot
	def shutdown(self):
		rospy.loginfo("Stop TurtleBot")
		# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
		# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		rospy.sleep(10)


if __name__ == '__main__':
	try:
		BatteryManagement()
	except rospy.ROSInterruptException:
		pass