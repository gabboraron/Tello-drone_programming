# -*- coding: utf-8 -*-
# @Author: sandor
# @Date:   2023-06-11 11:44:32
# @Last Modified by:   sandor
# @Last Modified time: 2023-06-11 11:49:42
#
# based on: https://github.com/damiafuentes/DJITelloPy#simple-example


from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

#tello.move_left(100)
tello.rotate_counter_clockwise(180)
tello.rotate_clockwise(180)
#tello.move_forward(100)

tello.land()