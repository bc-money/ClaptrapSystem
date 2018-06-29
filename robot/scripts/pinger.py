#!/usr/bin/env python

import subprocess
import os
import rospy

#tiny script to ping turtlebot
def ping():
	rospy.init_node('pinger', anonymous=False)
	#rospy.on_shutdown(shutdown)
	while not rospy.is_shutdown():
		hostname = "10.1.108.84"
		response = os.system("ping -c 1 " + hostname)
		print(response)
		rospy.sleep(10)

# def shutdown():
# 	print("ending ping program")
# 	rospy.sleep(1)

if __name__ == '__main__':
	ping()