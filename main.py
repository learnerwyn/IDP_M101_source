# Run this file in the competition
from machine import Pin, PWM
import detection_module
import motion_control
from motion_control import Motor
from time import sleep
from libs.tiny_code_reader.tiny_code_reader import TinyCodeReader
from libs.VL53L0X.VL53L0X import VL53L0X

# Set the two motors information, detailed PIN number subject to change here
# All the modules which have actions on the motors have arguments (motor_left, motor_right)
motor_left = Motor(dirPin=4, PWMPin=5)  # Motor 1 is controlled from Motor Driv2 #1, which is on GP4/5
motor_right = Motor(dirPin=4, PWMPin=5)