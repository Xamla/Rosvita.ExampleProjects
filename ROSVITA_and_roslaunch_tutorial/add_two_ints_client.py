#!/usr/bin/env python3

import re
import rospy

# imports the AddTwoInts service 
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsRequest

service_name = 'roslaunch_tutorial/add_two_ints'

def add_two_ints_client(x: int, y: int)->int:

    if (re.sub('[^A-Za-z0-9]+', '', rospy.get_name()) == 'unnamed'):
        rospy.init_node('rospy_node', anonymous=True)

    # block until the add_two_ints service is available
    # or time out is exceeded
    rospy.wait_for_service(service_name, timeout=3.0)
    
    # create a handle to the add_two_ints service
    add_two_ints = rospy.ServiceProxy(service_name, AddTwoInts)
    
    resp = add_two_ints.call(AddTwoIntsRequest(x, y))
    
    return resp.sum
