from machine import Pin, PWM
from utime import sleep

from motion_control import go_forward, go_back, turn_around, turn_left_90, turn_right_90, stop_the_car, adjust_to_left, adjust_to_right
from motion_control import Motor
from detection_module import qr_code_reader, distance_sensing, straight_line_detection

# Input the pin numbers down here
motor_left = Motor(dirPin=4, PWMPin=5)  # Motor 1 is controlled from Motor Driv2 #1, which is on GP4/5
motor_right = Motor(dirPin=4, PWMPin=5)

def test1(motor_left, motor_right):
    # test 1: go forward for 5 sec and stop and then go reverse
    go_forward(motor_left, motor_right, 30)
    sleep(5)
    stop_the_car(motor_left, motor_right)
    go_back(motor_left, motor_right, 30)

def test2(motor_left, motor_right):
    # test 2: turn left and then turn right and then turn around
    turn_left_90(motor_left, motor_right)
    sleep(5)
    turn_right_90(motor_left, motor_right)
    sleep(5)
    turn_around(motor_left, motor_right)
    
def test3(motor_left, motor_right):
    # test 3: adjust the car to the left and right
    go_forward(motor_left, motor_right, 50)
    sleep(3)
    adjust_to_left(motor_left, motor_right)
    go_forward(motor_left, motor_right, 50)
    sleep(3)
    adjust_to_right(motor_left, motor_right)
    go_forward(motor_left, motor_right, 50)
    sleep(3)
    stop_the_car(motor_left, motor_right)
    
def test4(motor_left, motor_right):
    # test 4: reading the qr code while moving, place the qr code a distance in front the bot before running this test
    go_forward(motor_left, motor_right, 50)
    code = None
    while code == None:
        code = qr_code_reader()
        if code != None:
            print(code)
    stop_the_car(motor_left,motor_right)
    
def test5(motor_left, motor_right):
    # test 5: reading distance while moving
    go_forward(motor_left, motor_right, 50)
    distance = 2000
    while distance > 200 :
        try:
            distance = int(distance_sensing())
        except:
            distance = None
        print(distance)
    stop_the_car(motor_left,motor_right) # stop the car while the distance is 200 mm
    
def test6(motor_left, motor_right):
    # test6: put the bot on a straight white line, test the straight line sensing
    straight, temp = straight_line_detection()
    if straight == True:
        go_forward(motor_left, motor_right, 50)
    while straight == True:
        straight, temp = straight_line_detection()
    stop_the_car(motor_left,motor_right) # stop the car while not following the straight line

if __name__ == "__main__":
    test1()