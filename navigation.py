import detection_module
import motion_control
import alignment
from time import sleep

#Starting sequence to make the robot leave the starting area and go to zone 1

def start_sequence(motor_left, motor_right):
    motion_control.go_forward(motor_left, motor_right, 80)
    sleep(0.5)
    straight, temp = detection_module.straight_line_detection()
    while temp != "junction_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()
    straight, temp = detection_module.straight_line_detection()
    while temp != "junction_detected":
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
        straight, temp = detection_module.straight_line_detection()e
    sleep(0.2)
    motion_control.stop_the_car(motor_left, motor_right)
    motion_control.turn_left_90(motor_left, motor_right)
    motion_control.go_forward(motor_left, motor_right, 80)
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
                    forklift.goToRaisedLevel()
            else:
                print(f"QR code found in zone 3: {code}")
                forklift.goToRaisedLevel()
        else:
            print(f"QR code found in zone 2: {code}")
            forklift.goToRaisedLevel()
    else:
        print(f"QR code found in zone 1: {code}")
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
    while temp != "right_detected" or temp != "left_detected" or temp != "junction_detected":
        straight, temp = detection_module.straight_line_detection()
        alignment.align_to_line(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 80)
    motion_control.stop_the_car(motor_left, motor_right)

    # Move to drop-off zone based on QR code data
    if "Rack A" in code:
        print("Moving to Rack A drop-off zone")
        motion_control.turn_right_90(motor_left, motor_right)
        motion_control.go_forward(motor_left, motor_right, 50)
        sleep(0.2)
        straight, temp = detection_module.straight_line_detection()
        while temp != "junction_detected":
            straight, temp = detection_module.straight_line_detection()
            alignment.align_to_line(motor_left, motor_right)
            motion_control.go_forward(motor_left, motor_right, 50)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_right_90(motor_left, motor_right)

    elif "Rack B" in code:
        print("Moving to Rack B drop-off zone")
        motion_control.turn_left_90(motor_left, motor_right)
        while detection_module.distance_sensing() > 100:
            motion_control.go_forward(motor_left, motor_right, 50)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_left_90(motor_left, motor_right)

    else:
        print("Unknown drop-off zone in QR code, returning to default path")
        motion_control.go_forward(motor_left, motor_right, 50)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)

        #placeholder for drop-off mechanism

        print("Activating drop-off mechanism")
        sleep(2)  # Simulate time taken for drop-off
        print("Drop-off complete")

    if "Lower" in code:
        # Placeholder for raising forklift to correct height
        print("Raising forklift to lower shelf height")
        sleep(2)  # Simulate time taken to raise forklift

        if "1" in code:
            while detection_module.distance_sensing() > 1000:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        elif "2" in code:
            while detection_module.distance_sensing() > 800:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        elif "3" in code:
            while detection_module.distance_sensing() > 600:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
        
        elif "4" in code:
            while detection_module.distance_sensing() > 400:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        elif "5" in code:
            while detection_module.distance_sensing() > 200:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
        
        elif "6" in code:
            while detection_module.distance_sensing() > 100:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        else:
            print("Oh no very bad")
        
        if "Rack A" in code:
            motion_control.turn_right_90(motor_left, motor_right)
        
        elif "Rack B" in code:
            motion_control.turn_left_90(motor_left, motor_right)

        else:
            print("Bad news bears")
    
        motion_control.go_forward(motor_left, motor_right, 50)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)

        # Placeholder for drop-off mechanism
        print("Activating drop-off mechanism")
        sleep(2)  # Simulate time taken for drop-off
        print("Drop-off complete")

    elif "Upper" in code:
        while detection_module.distance_sensing() > 50:
            motion_control.go_forward(motor_left, motor_right, 50)
        motion_control.stop_the_car(motor_left, motor_right)

        if "Rack A" in code:
            motion_control.turn_right_90(motor_left, motor_right)
            while detection_module.distance_sensing() > 1000:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)

        elif "Rack B" in code:
            motion_control.turn_left_90(motor_left, motor_right)
            while detection_module.distance_sensing() > 1000:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        else:
            print("Now we're really in trouble")

        while detection_module.distance_sensing() > 50 or detection_module.distance_sensing() is None:
            motion_control.go_forward(motor_left, motor_right, 100)
        motion_control.stop_the_car(motor_left, motor_right)

        if "Rack A" in code:
            motion_control.turn_right_90(motor_left, motor_right)
            while detection_module.distance_sensing() > 100:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)
            
        elif "Rack B" in code:
            motion_control.turn_left_90(motor_left, motor_right)
            while detection_module.distance_sensing() > 100:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        else:
            print("This is getting out of hand")

        if "1" in code:
            while detection_module.distance_sensing() > 1000:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        elif "2" in code:
            while detection_module.distance_sensing() > 800:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
        
        elif "3" in code:
            while detection_module.distance_sensing() > 600:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        elif "4" in code:
            while detection_module.distance_sensing() > 400:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        elif "5" in code:
            while detection_module.distance_sensing() > 200:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        elif "6" in code:
            while detection_module.distance_sensing() > 100:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)

        else:
            print("We are doomed")

        if "Rack A" in code:
            motion_control.turn_left_90(motor_left, motor_right)

        elif "Rack B" in code:
            motion_control.turn_right_90(motor_left, motor_right)

        else:
            print("Help me")

        motion_control.go_forward(motor_left, motor_right, 50)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)

        # Placeholder for drop-off mechanism
        print("Activating drop-off mechanism")
        sleep(2)  # Simulate time taken for drop-off
        print("Drop-off complete")

        motion_control.go_back(motor_left, motor_right, 50)
        sleep(1)
        motion_control.stop_the_car(motor_left, motor_right)


    else:
        print("Invalid level in QR code, aborting unloading sequence")

def return_sequence(motor_left, motor_right, code, sensor1, sensor2, sensor3, sensor4):
    print("Returning to starting area")

    if "Rack A" in code:
        motion_control.turn_left_90(motor_left, motor_right)

    elif "Rack B" in code:
        motion_control.turn_right_90(motor_left, motor_right)

    else:   
        print("We are cooked")

    if "Lower" in code:
        while detection_module.distance_sensing() < 1850:
            motion_control.go_back(motor_left, motor_right, 50)
        motion_control.stop_the_car(motor_left, motor_right)

        if "Rack A" in code:
            motion_control.turn_around(motor_left, motor_right)

        elif "Rack B" in code:
            motion_control.turn_left(motor_left, motor_right)
            while detection_module.distance_sensing() > 100:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        else:
            print("Oh no we're lost")
    
    elif "Upper" in code:
        while detection_module.distance_sensing() > 100:
            motion_control.go_forward(motor_left, motor_right, 50)
        motion_control.stop_the_car(motor_left, motor_right)

        if "Rack A" in code:
            motion_control.turn_left_90(motor_left, motor_right)
            while detection_module.distance_sensing() > 500:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_left_90(motor_left, motor_right)

        elif "Rack B" in code:
            motion_control.turn_right_90(motor_left, motor_right)
            while detection_module.distance_sensing() > 500:
                motion_control.go_forward(motor_left, motor_right, 50)
            motion_control.stop_the_car(motor_left, motor_right)
            motion_control.turn_right_90(motor_left, motor_right)

        else:
            print("Now we're really in trouble")

        while sensor1.value() == 0 or sensor4.value() == 0:
            motion_control.go_forward(motor_left, motor_right, 20)
        motion_control.stop_the_car(motor_left, motor_right)

        while detection_module.distance_sensing() > 200:
            motion_control.go_forward(motor_left, motor_right, 20)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_left_90(motor_left, motor_right)

        while detection_module.distance_sensing() > 200:
            motion_control.go_forward(motor_left, motor_right, 50)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_right_90(motor_left, motor_right)

        while detection_module.distance_sensing() < 1850:
            motion_control.go_back(motor_left, motor_right, 50)
        motion_control.stop_the_car(motor_left, motor_right)
        motion_control.turn_around(motor_left, motor_right)

    else:
        print("Something has gone terribly wrong")
     

def ending_sequence(motor_left, motor_right):
    print("Executing ending sequence to return to starting area")

    motion_control.turn_left_90(motor_left, motor_right)
    while detection_module.distance_sensing() > 1000:
        motion_control.go_forward(motor_left, motor_right, 50)
    motion_control.stop_the_car(motor_left, motor_right)
    motion_control.turn_right_90(motor_left, motor_right)
    motion_control.go_forward(motor_left, motor_right, 50)
    sleep(2)
    motion_control.stop_the_car(motor_left, motor_right)
    motion_control.turn_around(motor_left, motor_right)