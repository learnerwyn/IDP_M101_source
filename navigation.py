import detection_module
import motion_control
from time import sleep

#Starting sequence to make the robot leave the starting area and go to zone 1

def start_sequence(motor_left, motor_right):
    motion_control.go_forward(motor_left, motor_right,50)
    sleep(1)  # Move forward for 2 seconds

    #now stop when black line is detected

    while detection_module.straight_line_detection():
        sleep(0.1)
    motion_control.stop_the_car(motor_left, motor_right)

    #Now the bot is at the black line, turn left 90 degrees to face zone 1

    motion_control.turn_left_90(motor_left, motor_right)

    # Now move forward until the black line is detected again

    motion_control.go_forward(motor_left, motor_right, 50)
    while detection_module.straight_line_detection():
        sleep(0.1)
    motion_control.stop_the_car(motor_left, motor_right)

    # Lastly turn left 90 degrees to face zone 1

    motion_control.turn_left_90(motor_left, motor_right)

    # Note that this is very rough, and will depend greatly on testing and postion of the line sensors on the bot. 
    # May need to slightly adjust the bot before turning due to sensor placement

# Default path for normal operation from zone 1 to zone 4

def default_path(motor_left, motor_right):
    # read qr code in zone 1
    # if qr code isnt read, go to zone 2
    # otherwise end default path and leave default path function
    # then turn towards zone 2 and read qr code there
    # repeat process for zones 3 and 4. then return to zone 1 if nothing in zone 4
    motion_control.go_forward(50)
    sleep(1)
    motion_control.stop_the_car(motor_left, motor_right)
    code = detection_module.qr_code_reader()
    if code is None:
        motion_control.go_back(motor_left, motor_right, 50)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_left_90(motor_left, motor_right)
        while detection_module.distance_sensing() > 1850:
            motion_control.go_forward(motor_left, motor_right,50)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_right_90(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 50)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)
        code = detection_module.qr_code_reader()
        if code is None:
            motion_control.go_back(motor_left, motor_right, 50)
            sleep(1)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)
            while detection_module.distance_sensing() > 400:
                motion_control.go_forward(motor_left, motor_right,50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right,50)
            sleep(1)
            motion_control.stop_the_car(motor_left, motor_right)
            code = detection_module.qr_code_reader()
            if code is None:
                motion_control.go_back(motor_left, motor_right,50)
                sleep(1)
                motion_control.stop_the_car(motor_left, motor_right)
                motion_control.turn_left_90(motor_left, motor_right)
                while detection_module.distance_sensing() > 100:
                    motion_control.go_forward(motor_left, motor_right, 50)
                motion_control.stop_the_car(motor_left, motor_right)
                motion_control.turn_right_90(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 50)
                sleep(1)
                motion_control.stop_the_car(motor_left, motor_right)
                code = detection_module.qr_code_reader()
                if code is None:
                    print("No QR codes found in any zone, returning to zone 1")
                    motion_control.go_back(motor_left, motor_right,50)
                    sleep(1)
                    motion_control.stop_the_car(motor_left, motor_right)
                    motion_control.turn_right_90(motor_left, motor_right)
                    while detection_module.distance_sensing() > 100:
                        motion_control.go_forward(motor_left, motor_right, 50)
                    motion_control.stop_the_car(motor_left, motor_right)
                    motion_control.turn_left_90(motor_left, motor_right)
                else:
                    print(f"QR code found in zone 4: {code}")
            else:
                print(f"QR code found in zone 3: {code}")
        else:
            print(f"QR code found in zone 2: {code}")
    else:
        print(f"QR code found in zone 1: {code}")





 