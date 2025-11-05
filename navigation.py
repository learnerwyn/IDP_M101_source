import detection_module
import motion_control
import alignment
from time import sleep

#Starting sequence to make the robot leave the starting area and go to zone 1

def start_sequence(motor_left, motor_right):

    #drive forward out of starting bay, sleeping after the first junction to avoid stopping on it, then stopping at the second junction
    motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)
    straight, temp = detection_module.straight_line_detection()
    while temp != "junction_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
    sleep(0.2)
    straight, temp = detection_module.straight_line_detection()
    while temp != "junction_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
    sleep(0.2)
    motion_control.stop_the_car(motor_left, motor_right)

    #turn left to go to zone 1
    motion_control.turn_left_90(motor_left, motor_right)
    motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)
    straight, temp = detection_module.straight_line_detection()
    while temp != "junction_detected":
        straight, temp = detection_module.straight_line_detection()
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)
    motion_control.stop_the_car(motor_left, motor_right)
    motion_control.turn_left_90(motor_left, motor_right)

# Default path for normal operation from zone 1 to zone 4

def default_path(motor_left, motor_right, forklift):
    code = None
    #enter bay 1 and read code
    motion_control.go_forward(motor_left, motor_right, 80)
    straight, temp = detection_module.straight_line_detection()
    while temp != "junction_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
        if code == None:
            try:
                code = detection_module.qr_code_reader()
            except:
                code = None
    motion_control.stop_the_car(motor_left, motor_right)
    
    if code is None:
        #if code is not read, back out of bay 1
        motion_control.turn_around(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
        while temp != "right_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left,motor_right)
        motion_control.turn_right_90(motor_left, motor_right)
        
        #go to bay 2 entrance
        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "right_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_right_90(motor_left, motor_right)
        
        #enter bay 2 and scan code
        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "junction_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
            if code == None:
                try:
                    code = detection_module.qr_code_reader()
                except:
                    code = None
        motion_control.stop_the_car(motor_left, motor_right)
        
        if code is None:
            #if no code, back out of bay 2
            motion_control.turn_around(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "junction_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)

            #go to bay 3
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)

            straight, temp = detection_module.straight_line_detection()
            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()  

            sleep(0.4)
            straight, temp = detection_module.straight_line_detection()

            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)
            
            #enter bay 3 and scan
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "junction_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
                if code == None:
                    try:
                        code = detection_module.qr_code_reader()
                    except:
                        code = None
            motion_control.stop_the_car(motor_left, motor_right)
            
            if code is None:
                #if no code, back out of bay 3
                motion_control.turn_around(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                sleep(0.4)
                straight, temp = detection_module.straight_line_detection()
                while temp != "junction_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                sleep(0.3)
                motion_control.stop_the_car(motor_left, motor_right)
                motion_control.turn_right_90(motor_left, motor_right)

                #go to bay 4
                motion_control.go_forward(motor_left, motor_right, 80)
                sleep(0.2)
                straight, temp = detection_module.straight_line_detection()
                while temp != "junction_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                sleep(0.2)
                motion_control.stop_the_car(motor_left, motor_right)
                motion_control.turn_right_90(motor_left, motor_right)

                #enter bay 4 and scan
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
                while temp != "junction_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                    if code == None:
                        try:
                            code = detection_module.qr_code_reader()
                        except:
                            code = None
                motion_control.stop_the_car(motor_left, motor_right)
                
                if code is None:
                    #if no code, back out of bay 4
                    motion_control.turn_around(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    sleep(0.2)
                    straight, temp = detection_module.straight_line_detection()
                    while temp != "left_detected":
                        alignment.align_to_line(motor_left, motor_right)
                        motion_control.go_forward(motor_left, motor_right, 80)
                        straight, temp = detection_module.straight_line_detection()
                    sleep(0.2)
                    motion_control.stop_the_car(motor_left, motor_right)
                    motion_control.turn_left_90(motor_left, motor_right)

                    #go to bay 1
                    motion_control.go_forward(motor_left, motor_right, 80)
                    sleep(0.2)
                    straight, temp = detection_module.straight_line_detection()
                    while temp != "junction_detected":
                        alignment.align_to_line(motor_left, motor_right)
                        motion_control.go_forward(motor_left, motor_right, 80)
                        straight, temp = detection_module.straight_line_detection()
                    sleep(0.2)
                    motion_control.stop_the_car(motor_left, motor_right)
                    motion_control.turn_left_90(motor_left, motor_right)
                
                else:
                    print(f"QR code found in zone 4: {code}")
                    motion_control.go_forward(motor_left, motor_right, 30)
                    sleep(0.2)
                    motion_control.stop_the_car(motor_left, motor_right)
                    forklift.goToRaisedLevel()
            else:
                print(f"QR code found in zone 3: {code}")
                motion_control.go_forward(motor_left, motor_right, 30)
                sleep(0.2)
                motion_control.stop_the_car(motor_left, motor_right)
                forklift.goToRaisedLevel()
        else:
            print(f"QR code found in zone 2: {code}")
            motion_control.go_forward(motor_left, motor_right, 30)
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            forklift.goToRaisedLevel()
    else:
        print(f"QR code found in zone 1: {code}")
        motion_control.go_forward(motor_left, motor_right, 30)
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
        forklift.goToRaisedLevel()
    return code



# Sequence for when QR code is found to pick up and drop off the item

def unloading_sequence(motor_left, motor_right, forklift, code):
    print(f"Starting unloading sequence for QR code: {code}")

    # Placeholder for pickup mechanism

    print("Activating pickup mechanism")
    sleep(2)  # Simulate time taken for pickup
    print("Pickup complete")

    motion_control.turn_around(motor_left, motor_right)
    motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)
    straight, temp = detection_module.straight_line_detection()
    while temp != "right_detected" and temp != "left_detected" and temp != "junction_detected":
        straight, temp = detection_module.straight_line_detection()
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)
    motion_control.stop_the_car(motor_left, motor_right)

    # Move to drop-off zone based on QR code data
    if "Rack A" in code:
        if temp != "right_detected":
            motion_control.turn_left_90(motor_left, motor_right)
            print("Moving to front of bay 1")
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "junction_detected":
                straight, temp = detection_module.straight_line_detection()
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)
        else:
            print("Already at front of bay 1")

    elif "Rack B" in code:
        if temp != "left_detected":
            motion_control.turn_right_90(motor_left, motor_right)
            print("Moving to front of bay 4")
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "junction_detected":
                straight, temp = detection_module.straight_line_detection()
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)
        else:
            print("Already at front of bay 4")

    else:
        print("Invalid rack in QR code, returning to default path")
        distance = detection_module.distance_sensing()
        if distance is not None and distance > 200:
            print("Moving to front of bay 1")
            motion_control.turn_left_90(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "junction_detected":
                straight, temp = detection_module.straight_line_detection()
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)
        else:
            print("Already at front of bay 1")
            motion_control.turn_around(motor_left, motor_right)
            code = None
            return

    if "Lower" in code:

        counter = 0

        if "Rack B" in code:

            if "1" in code:
                counter = 0

            elif "2" in code:
                counter = 1

            elif "3" in code:
                counter = 2

            elif "4" in code:
                counter = 3

            elif "5" in code:
                counter = 4
        
            elif "6" in code:
                counter = 5

            else:
                print("Oh no very bad")
            
        elif "Rack A" in code:

            if "1" in code:
                counter = 5

            elif "2" in code:
                counter = 4

            elif "3" in code:
                counter = 3

            elif "4" in code:
                counter = 2

            elif "5" in code:
                counter = 1
        
            elif "6" in code:
                counter = 0

            else:
                print("Oh no very bad")

        
        if "Rack A" in code:
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            while counter > 0:
                straight, temp = detection_module.straight_line_detection()
                while temp != "right_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                sleep(0.4)
                counter -= 1
            straight, temp = detection_module.straight_line_detection()
            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)
        
        elif "Rack B" in code:
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            while counter > 0:
                straight, temp = detection_module.straight_line_detection()
                while temp != "left_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                sleep(0.4)
                counter -= 1
            straight, temp = detection_module.straight_line_detection()
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        else:
            print("Bad news bears")
    
        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)

        # Placeholder for drop-off mechanism
        print("Activating drop-off mechanism")
        sleep(2)  # Simulate time taken for drop-off
        print("Drop-off complete")

    elif "Upper" in code:
        distance = detection_module.distance_sensing()
        straight, temp = detection_module.straight_line_detection()

        if "Rack A" in code:
            counter = 6
            while counter > 0:
                while temp != "right_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                counter -= 1
                sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)

            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)

        elif "Rack B" in code:
            counter = 6
            while counter > 0:
                while temp != "left_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                counter -= 1
                sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        else:
            print("Now we're really in trouble")

        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "junction_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)

        if "Rack A" in code:
            motion_control.turn_right_90(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)
            
        elif "Rack B" in code:
            motion_control.turn_left_90(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        else:
            print("This is getting out of hand")

        counter = 0

        if "Rack B" in code:

            if "1" in code:
                counter = 5

            elif "2" in code:
                counter = 4

            elif "3" in code:
                counter = 3

            elif "4" in code:
                counter = 2

            elif "5" in code:
                counter = 1
        
            elif "6" in code:
                counter = 0

            else:
                print("Oh no very bad")

        elif "Rack A" in code:
            if "1" in code:
                counter = 0

            elif "2" in code:
                counter = 1

            elif "3" in code:
                counter = 2

            elif "4" in code:
                counter = 3

            elif "5" in code:
                counter = 4
        
            elif "6" in code:
                counter = 5

            else:
                print("Oh no very bad")

        
        if "Rack A" in code:
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            while counter > 0:
                straight, temp = detection_module.straight_line_detection()
                while temp != "left_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                sleep(0.4)
                counter -= 1
            straight, temp = detection_module.straight_line_detection()
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)
        
        elif "Rack B" in code:
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            while counter > 0:
                straight, temp = detection_module.straight_line_detection()
                while temp != "right_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                sleep(0.4)
                counter -= 1
            straight, temp = detection_module.straight_line_detection()
            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)


        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)

        # Placeholder for drop-off mechanism
        print("Activating drop-off mechanism")
        sleep(2)  # Simulate time taken for drop-off
        print("Drop-off complete")

    else:
        print("Invalid level in QR code, aborting unloading sequence")

def return_sequence(motor_left, motor_right, code):
    print("Returning to starting area")

    if code == None:
        return

    else:
        motion_control.go_back(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "junction_detected" and temp != "left_detected" and temp != "right_detected":
            motion_control.go_back(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)

    if "Rack A" in code and "Lower" in code:
        motion_control.turn_right_90(motor_left, motor_right)

    elif "Rack B" in code and "Lower" in code:
        motion_control.turn_left_90(motor_left, motor_right)

    elif "Rack A" in code and "Upper" in code:
        motion_control.turn_left_90(motor_left, motor_right)

    elif "Rack B" in code and "Upper" in code:
        motion_control.turn_right_90(motor_left, motor_right)

    else:   
        print("We are cooked")

    if "Lower" in code:
        distance = detection_module.distance_sensing()
        straight, temp = detection_module.straight_line_detection()
        while distance > 500 or temp != "junction_detected" and temp != "left_detected" and temp != "right_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            distance = detection_module.distance_sensing()
            straight, temp = detection_module.straight_line_detection()
            distance = detection_module.distance_sensing()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
            

        if "Rack A" in code:
            print("Ready to start default path")

        elif "Rack B" in code:
            motion_control.turn_right_90(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "junction_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)
            print("Ready to start default path")

        else:
            print("Oh no we're lost")
    
    elif "Upper" in code:

        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()

        if "Rack A" in code:
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        elif "Rack B" in code:
            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)

            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while temp != "right_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)

        else:
            print("Now we're really in trouble")

        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "junction_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_left(motor_left, motor_right)

        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "left_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_left_90(motor_left, motor_right)

        motion_control.go_forward(motor_left, motor_right,80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        distance = detection_module.distance_sensing()
        while distance > 500 or temp != "left_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            distance = detection_module.distance_sensing()
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
        print("Ready to start default path")

    else:
        print("Something has gone terribly wrong")
     

def ending_sequence(motor_left, motor_right):
    print("Executing ending sequence to return to starting area")

    motion_control.turn_left_90(motor_left, motor_right)
    motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)

    straight, temp = detection_module.straight_line_detection()
    while temp != "right_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()  

    sleep(0.4)
    straight, temp = detection_module.straight_line_detection()

    while temp != "right_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
            
    sleep(0.2)
    motion_control.stop_the_car(motor_left, motor_right)
    motion_control.turn_right_90(motor_left, motor_right)
    motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)
    while temp != "junction_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
    sleep(0.5)
    motion_control.stop_the_car(motor_left, motor_right)
    motion_control.turn_around(motor_left, motor_right)