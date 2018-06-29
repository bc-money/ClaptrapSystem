#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PointStamped

def talker():
    pub = rospy.Publisher('/clicked_point', PointStamped, queue_size = 10)
    rospy.init_node('infinite_rectangle', anonymous=True)
    rate = rospy.Rate(1)

    pt1 = PointStamped()
    pt2 = PointStamped()
    pt3 = PointStamped()
    pt4 = PointStamped()
    pt5 = PointStamped()
    pt6 = PointStamped()

    pt1.point.x = 10.0
    pt1.point.y = -10.0
    pt1.point.z = 0.0
    pt1.header.frame_id = "map"
    pt1.header.seq = 0
    pt1.header.stamp = rospy.Time.now()

    pt2.point.x = -10.0
    pt2.point.y = -10.0
    pt2.point.z = 0.0
    pt2.header.frame_id = "map"
    pt2.header.seq = 1
    pt2.header.stamp = rospy.Time.now()

    pt3.point.x = -10.0
    pt3.point.y = 10.0
    pt3.point.z = 0.0
    pt3.header.frame_id = "map"
    pt3.header.seq = 2
    pt3.header.stamp = rospy.Time.now()

    pt4.point.x = 10.0
    pt4.point.y = 10.0
    pt4.point.z = 0.0
    pt4.header.frame_id = "map"
    pt4.header.seq = 3
    pt4.header.stamp = rospy.Time.now()

    pt5.point.x = 10.0
    pt5.point.y = -10.0
    pt5.point.z = 0.0
    pt5.header.frame_id = "map"
    pt5.header.seq = 4
    pt5.header.stamp = rospy.Time.now()

    pt6.point.x = 0.0
    pt6.point.y = 0.0
    pt6.point.z = 0.0
    pt6.header.frame_id = "map"
    pt6.header.seq = 5
    pt6.header.stamp = rospy.Time.now()

    rate.sleep()
    rospy.loginfo(pt1)
    pub.publish(pt1)
    rate.sleep()

    rospy.loginfo(pt2)
    pub.publish(pt2)
    rate.sleep()

    rospy.loginfo(pt3)
    pub.publish(pt3)
    rate.sleep()

    rospy.loginfo(pt4)
    pub.publish(pt4)
    rate.sleep()

    rospy.loginfo(pt5)
    pub.publish(pt5)
    rate.sleep()

    rospy.loginfo(pt6)
    pub.publish(pt6)
    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
