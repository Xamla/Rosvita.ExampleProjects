import argparse
import re
import numpy as np
from typing import Tuple, Union
from lib.python.setup_stereo_laser_line_client import (StereoLaserLineClientParameter,
                                                       setup_stereo_laser_line_client)

import rospy

from xamla_vision import GeniCamCaptureClient, SimulatedCaptureClient
from xamla_vision.stereo_laser_line_client import StereoLaserLineClient

stereo_laser_line_client = None


def main(args):
    try:
        master = rospy.get_master()
        master.getSystemState()
    except ConnectionRefusedError:
        print('Please start ROS to run this tutorial script')

    # check if ros is
    if (re.sub('[^A-Za-z0-9]+', '', rospy.get_name()) == 'unnamed'):
        rospy.init_node('StereoLaserLineClient', anonymous=True)

    parameters = StereoLaserLineClientParameter(
        args.left_cam_serial,
        args.right_cam_serial,
        args.cam_with_laser_serial,
        args.laser_io_port,
        args.stereo_calibration_file_path,
        args.max_depth,
        args.axis
    )

    client, info_string = setup_stereo_laser_line_client(parameters)
    print(info_string)

    points_3d, left_exists = client(exposure_times=[args.exposure_time,
                                                    args.exposure_time],
                                    debug_mode=args.debug_mode)

    return points_3d


def call_from_graph() -> str:
    try:
        master = rospy.get_master()
        master.getSystemState()
    except ConnectionRefusedError:
        return 'Please start ROS to run this tutorial graph'

    ros_init = ', rospy is already initialized'
    if (re.sub('[^A-Za-z0-9]+', '', rospy.get_name()) == 'unnamed'):
        ros_init = ', initialize rospy'
        rospy.init_node('StereoLaserLineClient', anonymous=True)

    parameters = StereoLaserLineClientParameter(
        '4103130811',
        '4103189394',
        '4103130811',
        2,
        './calibration/left_arm_cameras/stereo_cams_4103130811_4103189394.t7',
        0.55,
        1
    )

    client, info_string = setup_stereo_laser_line_client(parameters)
    print(info_string)

    points_3d, left_exists = client(exposure_times=[15000,
                                                    15000],
                                    debug_mode=True)

    return info_string + ros_init


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='example how to use the'
                                                 ' stereo laser line client'
                                                 ' (standalone)')

    parser.add_argument('--left_cam_serial', type=str, required=True,
                        help='serial number of left camera in stereo setup')

    parser.add_argument('--right_cam_serial', type=str, required=True,
                        help='serial number of right camera in stereo setup')

    parser.add_argument('--stereo_calibration_file_path', type=str, required=True,
                        help='path to stereo calibration in t7 or xml file')

    parser.add_argument('--cam_with_laser_serial', type=str, required=True,
                        help='serial number of camera with which the line'
                        ' laser is controlled')

    parser.add_argument('--laser_io_port', type=int, required=True,
                        help='io port on which the line laser is connected')

    parser.add_argument('--max_depth', type=float, required=False, default=0.55,
                        help='max distance in z-axis of resulting 3d from'
                        ' left image origin')

    parser.add_argument('--axis', type=int, required=False, default=1,
                        help='set axis to 1 if laser line is projected along'
                        ' columns (y axis) else to 0 when laser line is'
                        ' projected along rows (x axis)')

    parser.add_argument('--debug_mode', type=bool, required=False, default=True,
                        help='if debug_mode is true visualize captured diff images '
                        'and resulting 3d points of the laser line')

    parser.add_argument('--exposure_time', type=int, required=False, default=15000,
                        help='exposure time of cameras in microseconds')

    # args = parser.parse_args()

    args = parser.parse_args(
        [
            '--left_cam_serial', '4103130811',
            '--right_cam_serial', '4103189394',
            '--stereo_calibration_file_path', './calibration/left_arm_cameras/stereo_cams_4103130811_4103189394.t7',
            '--cam_with_laser_serial', '4103130811',
            '--laser_io_port', '2',
            '--exposure_time', '15000'
        ]
    )

    main(args)
