import detection_module
import motion_control
from time import sleep

#Starting sequence to make the robot leave the starting area and go to zone 1

def start_sequence():
    motion_control.go_forward(50)
    sleep(1)  # Move forward for 2 seconds

    #now stop when black line is detected

    while detection_module.straight_line_detection():
        sleep(0.1)
    motion_control.stop_the_car()

    #Now the bot is at the black line, turn left 90 degrees to face zone 1

    motion_control.turn_left_90()

    # Now move forward until the black line is detected again

    motion_control.go_forward(50)
    while detection_module.straight_line_detection():
        sleep(0.1)
    motion_control.stop_the_car()

    # Lastly turn left 90 degrees to face zone 1

    motion_control.turn_left_90()

    # Note that this is very rough, and will depend greatly on testing and postion of the line sensors on the bot. 
    # May need to slightly adjust the bot before turning due to sensor placement

# Default path for normal operation from zone 1 to zone 4

def default_path():
    # read qr code in zone 1
    # if qr code isnt read, go to zone 2
    # otherwise end default path and follow qr code instructions
    # then turn towards zone 2 and read qr code there
    # repeat process for zones 3 and 4. then return to zone 1 if nothing in zone 4
    code = detection_module.qr_code_reader()
    if code is None:
        motion_control.turn_left_90()
        while detection_module.distance_sensing() > 100:
            motion_control.go_forward(50)
        motion_control.stop_the_car()
        motion_control.turn_right_90()
        code = detection_module.qr_code_reader()
        if code is None:
            motion_control.turn_left_90()
            while detection_module.distance_sensing() > 50:
                motion_control.go_forward(50)
            motion_control.stop_the_car()
            motion_control.turn_right_90()
            code = detection_module.qr_code_reader()
            if code is None:
                motion_control.turn_left_90()
                while detection_module.distance_sensing() > 25:
                    motion_control.go_forward(50)
                motion_control.stop_the_car()
                motion_control.turn_right_90()
                code = detection_module.qr_code_reader()
                if code is None:
                    print("No QR codes found in any zone, returning to zone 1")
                    motion_control.turn_right_90()
                    while detection_module.distance_sensing() > 25:
                        motion_control.go_forward(50)
                    motion_control.stop_the_car()
                    motion_control.turn_left_90()
                else:
                    print(f"QR code found in zone 4: {code}")
            else:
                print(f"QR code found in zone 3: {code}")
        else:
            print(f"QR code found in zone 2: {code}")
    else:
        print(f"QR code found in zone 1: {code}")



 