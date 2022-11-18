#!/usr/bin/env python

import numpy as np
import time
import cv2
from UR_Robot import UR_Robot
from scipy import optimize  


# User options (change me)
# --------------- Setup options ---------------
tcp_host_ip = '192.168.56.101' # IP and port to robot arm as TCP client (UR5)
tcp_port = 30003
#---------------------------------------------


# Move robot to home pose
print('Connecting to robot...')
robot = UR_Robot(tcp_host_ip,tcp_port, is_use_robotiq85=False, is_use_camera=False)
# robot.open_gripper()

# Slow down robot
robot.joint_acc = 1.4
robot.joint_vel = 1.05

# Make robot gripper point upwards
# robot.move_j([-np.pi, -np.pi/2, np.pi/2, 0, np.pi/2, np.pi])
# robot.move_j([(40 / 360.0) * 2 * np.pi, -(60 / 360.0) * 2 * np.pi,          # 标定准备姿态
#                           (-120 / 360.0) * 2 * np.pi, -(180 / 360.0) * 2 * np.pi,
#                           -(90 / 360.0) * 2 * np.pi, -(90 / 360.0) * 2 * np.pi])
grasp_home = [(16 / 360.0) * 2 * np.pi, (-83 / 360.0) * 2 * np.pi,          # 抓取起始姿态
                          (-65 / 360.0) * 2 * np.pi, (-120 / 360.0) * 2 * np.pi,
                          (90 / 360.0) * 2 * np.pi, (-75 / 360.0) * 2 * np.pi]
robot.move_j(grasp_home)
