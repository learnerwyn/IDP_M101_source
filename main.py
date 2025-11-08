# Run this file in the competition
from machine import Pin, PWM
import detection_module
import motion_control
import navigation
from motion_control import Motor
from forklift import Forklift
import time
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

forklift = Forklift(13)


# Start a timer for 4 ish minutes in order to complete parking sequence within time limit

#Set a timer for 270 seconds to allow for parking sequence

start_time = time.ticks_ms()
time_limit = 270000  # 270 seconds in milliseconds
end_time = start_time + time_limit

# Complete start sequence and move to zone 1

navigation.start_sequence(motor_left, motor_right)

while time.ticks_ms() < end_time:

    code = navigation.default_path(motor_left, motor_right, forklift)

    #when code has been found, carry out unloading sequence

    if code:

        navigation.unloading_sequence(motor_left, motor_right, forklift, code)

        #after unloading sequence, return to default path

        navigation.return_sequence(motor_left, motor_right, code)

        code = None

    else:

        continue

# After time limit is reached, carry out parking sequence

navigation.ending_sequence(motor_left, motor_right)
    


