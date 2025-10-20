import detection_module
import motion_control
from time import sleep

#Starting sequence to make the robot leave the starting area and go to zone 1

def start_sequence():
    motion_control.go_forward(50)
    sleep(2)  # Move forward for 2 seconds

    #now stop when black line is detected

    while detection_module.straight_line_detection():
        sleep(0.1)
    motion_control.stop_the_car()

    #Now the bot is at the black line, turn left 90 degrees to face zone 1

    motion_control.turn_left_90()

    # Now once again move forward until the black line is detected again

    motion_control.go_forward(50)
    while detection_module.straight_line_detection():
        sleep(0.1)
    motion_control.stop_the_car()

    # Lastly turn left 90 degrees to face zone 1

    motion_control.turn_left_90()

    # Note that this is very rough, and will depend greatly on testing and postion of the line sensors on the bot. 
    # May need to slightly adjust the bot before turning due to sensor placement
    # Also i think it would be better if the left and right sensors were aligned with the centre of the bot rather than towards
    # the front so that we dont need to adjust before turning