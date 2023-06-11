# -*- coding: utf-8 -*-
# @Author: sandor
# @Date:   2023-06-11 12:19:49
# @Last Modified by:   sandor
# @Last Modified time: 2023-06-11 12:20:05
# based on https://github.com/damiafuentes/DJITelloPy/blob/master/examples/take-picture.py

import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
cv2.imwrite("picture.png", frame_read.frame)

tello.land()