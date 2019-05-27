import rospy
import re


def main() -> str:
    try:
        master = rospy.get_master()
        master.getSystemState()
    except ConnectionRefusedError:
        return 'Please start ROS to run this tutorial graph'

    ros_init = 'rospy is already initialized'
    if (re.sub('[^A-Za-z0-9]+', '', rospy.get_name()) == 'unnamed'):
        ros_init = 'initialize rospy'
        rospy.init_node('rospy_node', anonymous=True)

    return ros_init
