from machine import Pin, PWM
from utime import sleep

from motion_control import go_forward, go_back, turn_around, turn_left_90, turn_right_90, stop_the_car, adjust_to_left, adjust_to_right
from motion_control import Motor

# Input the pin numbers down here
motor_left = Motor(dirPin=4, PWMPin=5)  # Motor 1 is controlled from Motor Driv2 #1, which is on GP4/5
motor_right = Motor(dirPin=4, PWMPin=5)

# test 1: go forward for 5 sec and stop and then go reverse
go_forward(motor_left, motor_right, 30)
sleep(5)
stop_the_car(motor_left, motor_right)
go_back(motor_left, motor_right, 30)

# test 2: turn left and then turn right and then turn around
turn_left_90(motor_left, motor_right)
sleep(5)
turn_right_90(motor_left, motor_right)
sleep(5)
turn_around(motor_left, motor_right)
