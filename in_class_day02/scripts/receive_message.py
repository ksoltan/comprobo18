#!/usr/bin/env python
""" Investigate receiving a message using a callback function """
from geometry_msgs.msg import PointStamped
import rospy

class ReceiveMessageNode(object):
    def __init__(self):
        rospy.init_node('receive_message')
        rospy.Subscriber("/my_point", PointStamped, self.process_point)

    def run(self):
        rospy.spin() # continue querying indefinitely

    # Callback for when message is received on my_point topic.
    def process_point(self, msg):
        print msg.header

if __name__ == "__main__":
    node = ReceiveMessageNode()
    node.run()
