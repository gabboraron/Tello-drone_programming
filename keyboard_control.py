# -*- coding: utf-8 -*-
# @Author: sandor
# @Date:   2023-06-11 11:44:32
# @Last Modified by:   sandor
# @Last Modified time: 2023-06-11 12:15:48
# based on: https://github.com/damiafuentes/DJITelloPy/blob/master/examples/manual-control-opencv.py

# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from djitellopy import Tello
import cv2, math, time
import threading

def get_frame_of_Tello():
    frame_read = tello.get_frame_read()
    return frame_read

def send_command_to_Tello():
    tello.takeoff()
    while True:
        key = cv2.waitKey(1) & 0xff
        if key == 27: # ESC
            break
        elif key == ord('w'):
            tello.move_forward(30)
        elif key == ord('s'):
            tello.move_back(30)
        elif key == ord('a'):
            tello.move_left(30)
        elif key == ord('d'):
            tello.move_right(30)
        elif key == ord('e'):
            tello.rotate_clockwise(30)
        elif key == ord('q'):
            tello.rotate_counter_clockwise(30)
        elif key == ord('r'):
            tello.move_up(30)
        elif key == ord('f'):
            tello.move_down(30)
    tello.land()

def show_camera_from_Tello():
    while True:     
        frame_read = tello.get_frame_read()
        img = frame_read.frame
        cv2.imshow("drone", img)



tello = Tello()
tello.connect()

tello.streamon()
t1 = threading.Thread(target=show_camera_from_Tello)
t2 = threading.Thread(target=send_command_to_Tello)

t1.start()
t2.start()

t2.join()
print("LANDED")

    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    #img = frame_read.frame
    #cv2.imshow("drone", img)

