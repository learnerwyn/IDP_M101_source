from machine import Pin, PWM
from utime import sleep
import detection_module
import motion_control

# Alignment procedure to ensure that the robot is properly aligned with the detected line
# If the front sensor does not detect the line, but either left or right sensor does, the robot will adjust its position accordingly.

def align_to_line():
    # Read the line sensors
    sensor4 = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Left sensor
    sensor3 = Pin(13, Pin.IN, Pin.PULL_DOWN)  # Front sensor
    sensor1 = Pin(14, Pin.IN, Pin.PULL_DOWN)  # Right sensor
        
    left_detected = sensor4.value()
    front_detected = sensor3.value()
    right_detected = sensor1.value()
        
    if front_detected:
        print("Aligned with the line.")
        detection_module.straight_line_detection()  # Update LED status
    elif left_detected:
        print("Line detected on the left. Adjusting position...")
        motion_control.turn_left(0.2)  # Turn left slightly
    elif right_detected:
        print("Line detected on the right. Adjusting position...")
        motion_control.turn_right(0.2)  # Turn right slightly
    else:
        print("No line detected. moving forward slightly to align centre of car to line and then stopping.")
        motion_control.go_forward(20)  # Move forward slightly
        motion_control.stop_the_car()
        
 