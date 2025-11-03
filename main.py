# Run this file in the competition
from machine import Pin, PWM
import detection_module
import motion_control
import navigation
from motion_control import Motor
from forklift import Forklift
from time import sleep
from libs.tiny_code_reader.tiny_code_reader import TinyCodeReader
from libs.VL53L0X.VL53L0X import VL53L0X

bot_state = motion_control.general_push_button()
# check the push button, until it is turned on
while bot_state == False:
    bot_state = motion_control.general_push_button() 

# Set the two motors information, detailed PIN number subject to change here
# All the modules which have actions on the motors have arguments (motor_left, motor_right)
motor_left = Motor(dirPin=7, PWMPin=6)  # Motor 1 is controlled from Motor Driv2 #1, which is on GP4/5
motor_right = Motor(dirPin=4, PWMPin=5)

forklift = Forklift(
    15, # servo 1 position pin
)


# Start a timer for 4 ish minutes in order to complete parking sequence within time limit


# Complete start sequence and move to zone 1
navigation.start_sequence(motor_left, motor_right)

# Complete default path repeatedly until QR code is found or time limit is reached
code = navigation.default_path()
while code == None:
    code = navigation.default_path()
navigation.unloading_sequence(motor_left, motor_right, forklift, code)
    

# When a QR code is found, complete unloading sequence based on the QR code data
# This includes a pickup mechanism, movement to the drop-off zone, and unloading mechanism


# When the time limit is reached, complete parking sequence to park in the starting area
