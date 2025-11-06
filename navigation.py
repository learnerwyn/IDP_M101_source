import detection_module
import motion_control
import alignment
from time import sleep
import forklift

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

                    #after successfully scanning code, move forward slightly and lower forklift to pick up box
                    #code is same irrespective of bay

                    print(f"QR code found in zone 4: {code}")
                    forklift.goToGroundLevel()
                    motion_control.go_forward(motor_left, motor_right, 30)
                    sleep(0.2)
                    motion_control.stop_the_car(motor_left, motor_right)
                    forklift.goToRaisedLevel()
            else:
                print(f"QR code found in zone 3: {code}")
                forklift.goToGroundLevel()
                motion_control.go_forward(motor_left, motor_right, 30)
                sleep(0.2)
                motion_control.stop_the_car(motor_left, motor_right)
                forklift.goToRaisedLevel()
        else:
            print(f"QR code found in zone 2: {code}")
            forklift.goToGroundLevel()
            motion_control.go_forward(motor_left, motor_right, 30)
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            forklift.goToRaisedLevel()
    else:
        print(f"QR code found in zone 1: {code}")
        forklift.goToGroundLevel() 
        motion_control.go_forward(motor_left, motor_right, 30)
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
        forklift.goToRaisedLevel()

    #return the code found, or None if no code was found
    return code



# Sequence for when QR code is found to pick up and drop off the item

def unloading_sequence(motor_left, motor_right, forklift, code):
    print(f"Starting unloading sequence for QR code: {code}")

    # Back out of the bay
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

    # Travel to the entrance of bay 1 if rack A is the destination
    # This works regardless of starting  bay    

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

    # Same, but for rack B and bay 4

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

    # similar to the code for rack A, but ends by facing into bay 1, the starting point for default path

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
        
    # Creates a counter in order to go down the correct turn on the rack
    # Different counters have to be used on each side due to the numbers being in reverse order on rack A

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

        # go forward and sleep on each turn until the counter reaches zero, then take the next turn
        
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
        
        # Similar, but for rack B it is a left turn

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

        # if it gets lost now, there is no way to recover, so print an error message
        # this applies to all further else statements with a humerous message in the function

        else:
            print("Bad news bears")

        # move into the bay and drop off the box
    
        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)

        forklift.goToGroundLevel()
        print("Drop-off complete")

    # use the same counter logic to entirely pass the lower rack and on take the turn to the upper rack at the end

    elif "Upper" in code:
        distance = detection_module.distance_sensing()
        straight, temp = detection_module.straight_line_detection()

        if "Rack A" in code:
            counter = 6
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
            counter = 6
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
            print("Now we're really in trouble")

        # move forward to the junction at the bottom of the ramp

        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "left_detected" and temp != "right_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)

        # face the ramp

        if "Rack A" in code:
            motion_control.turn_right_90(motor_left, motor_right)

        if "Rack B" in code:
            motion_control.turn_left_90(motor_left, motor_right)

        # drive up the ramp

        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "junction_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)

        # take the turn into the correct rack

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

        # code identical to lower rack drop-off from here, other than the fact that now rack B is in reverse order

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

        # once again, sleep until the counter reaches zero, then take the next turn
        
        if "Rack A" in code:
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
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
            straight, temp = detection_module.straight_line_detection()
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

        # move into bay and drop off box

        motion_control.go_forward(motor_left, motor_right, 80)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)

        forklift.goToGroundLevel()
        print("Drop-off complete")

    else:
        print("Invalid level in QR code, aborting unloading sequence")

def return_sequence(motor_left, motor_right, code):
    print("Returning to starting area")

    if code == None:
        return

    # Back out of the bay and reset forklift

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
        forklift.goToRaisedLevel()
        
    # make sure the robot is facing in the right direction to start the return journey

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

    # the counter logic is applied again but in reverse to get back to the loading area

    if "Lower" in code:

        if "Rack A" in code:

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

        elif "Rack B" in code:

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
            
        # move forward and sleep on each turn until the counter reaches zero
        # if rack A was visited, the bot is now in position to start the default path again
        # if rack B was visited, the bot must take an extra turn and drive to the start of bay 1

        if "Rack A" in code:
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while counter > 0:
                while temp != "left_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                counter -= 1
                sleep(0.4)
            straight, temp = detection_module.straight_line_detection()
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            sleep(0.2)
            motion_control.stop_the_car(motor_left, motor_right)
            print("Ready to start default path")

        elif "Rack B" in code:
            motion_control.go_forward(motor_left, motor_right, 80)
            sleep(0.2)
            straight, temp = detection_module.straight_line_detection()
            while counter > 0:
                while temp != "right_detected":
                    alignment.align_to_line(motor_left, motor_right)
                    motion_control.go_forward(motor_left, motor_right, 80)
                    straight, temp = detection_module.straight_line_detection()
                counter -= 1
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

        # the counter does not have to be used for the upper racks as the turn it needs to take is on the opposite side of the path to the rack

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

            # drive to the junction at the top of the ramp and face down

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

            # drive to the junction at the top of the ramp and face down

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

        # at this point the bot is on the same path regardless of which upper rack it visited, so it can drive the same way either way
        # drive down the ramp

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

        # drive to the turn in the top left corner of the warehouse

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

        # the counter logic is applied again to reach bay 1 and not stop at the turns in front of lower rack A

        motion_control.go_forward(motor_left, motor_right,80)
        sleep(0.2)
        counter = 6
        straight, temp = detection_module.straight_line_detection()
    
        while counter > 0:
            while temp != "left_detected":
                alignment.align_to_line(motor_left, motor_right)
                motion_control.go_forward(motor_left, motor_right, 80)
                straight, temp = detection_module.straight_line_detection()
            counter -= 1
            sleep(0.4)
        while temp != "left_detected":
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 80)
            straight, temp = detection_module.straight_line_detection()
        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)

        sleep(0.2)
        motion_control.stop_the_car(motor_left, motor_right)
        print("Ready to start default path")

    else:
        print("Something has gone terribly wrong")

# simple directions to take the bot back to the start area for the start of the default path

def ending_sequence(motor_left, motor_right):
    print("Executing ending sequence to return to starting area")

    motion_control.turn_left_90(motor_left, motor_right)
    motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.2)

    # sleeps on the first turn into bay 2, then goes into starting area and parks

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

    # now facing into starting area

    sleep(0.2)
    while temp != "junction_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
    sleep(0.5)
    motion_control.stop_the_car(motor_left, motor_right)
    motion_control.turn_around(motor_left, motor_right)