#!/usr/bin/env python
""" This script explores publishing ROS messages in ROS using Python """
from geometry_msgs.msg import PointStamped, Point
from std_msgs.msg import Header
import rospy

class TestMessageNode(object):
    def __init__(self):
        rospy.init_node("test_message")
        self.my_point_stamped = PointStamped(header = Header(stamp = rospy.Time.now(), frame_id = "odom"),
            point = Point(1.0, 2.0, 0.0))
        print(self.my_point_stamped)
        self.publisher = rospy.Publisher("/my_point", PointStamped, queue_size=10)

    def run(self):
        r = rospy.Rate(2)
        print("Starting run")
        while not rospy.is_shutdown():
            self.my_point_stamped.header.stamp = rospy.Time.now() # update timestamp
            self.publisher.publish(self.my_point_stamped) # publish timestamp
            print self.my_point_stamped
            r.sleep() # publish new timestamp every 2 seconds

if __name__ == "__main__":
    node = TestMessageNode()
    node.run()
