#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def submit():
    pub = rospy.Publisher('name', String, queue_size=10)
    rospy.init_node('submit', anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        naam = "Baibhav Vishal %s" % rospy.get_time()
        rospy.loginfo(naam)
        pub.publish(naam)
        rate.sleep()

if __name__ == '__main__':
    try:
        submit()
    except rospy.ROSInterruptException:
        pass
