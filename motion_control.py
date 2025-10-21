from machine import Pin, PWM
from time import sleep

class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
        
    def off(self):
        self.pwm.duty_u16(0)
        
    def Forward(self, speed):
        self.mDir.value(0)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

    def Reverse(self, speed):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))

# Set the two motors information, detailed PIN number subject to change here
# motor_left = Motor(dirPin=4, PWMPin=5)  # Motor 1 is controlled from Motor Driv2 #1, which is on GP4/5
# motor_right = Motor(dirPin=4, PWMPin=5)

def go_forward(motor_left, motor_right, speed):
    motor_left.Forward(speed)
    motor_right.Forward(speed)
    
def go_back(motor_left, motor_right, speed):
    motor_left.Reverse(speed)
    motor_right.Reverse(speed)

def stop_the_car(motor_left, motor_right):
    motor_left.off
    motor_right.off

def turn_right_90(motor_left, motor_right):
    
    print("Turn Right Start")
    speed = 30 # speed subject to adjustment
    motor_left.Forward(speed)
    motor_right.Reverse(speed)
    sleep(3) # time subject to adjustment
    motor_left.off()
    motor_right.off()
    print("Turn Right Finish")
    
def turn_left_90(motor_left, motor_right):
    
    print("Trun Left Start")
    speed = 30 # speed subject to adjustment
    motor_left.Reverse(speed)
    motor_right.Forward(speed)
    sleep(3) # time subject to adjustment
    motor_left.off()
    motor_right.off()
    print("Turn Left Finish")
    
def turn_around(motor_left, motor_right):
    
    print("Trun Around Start")
    speed = 30 # speed subject to adjustment
    motor_left.Reverse(speed)
    motor_right.Forward(speed)
    sleep(6) # time subject to adjustment
    motor_left.off()
    motor_right.off()
    print("Turn Around Finish")
    
def adjust_to_left(motor_left, motor_right):
    
    print("Adjusting position")
    motor_left.Forward(10)
    motor_right.Forward(30)
    sleep(0.5)
    motor_left.Forward(30)
    motor_right.Forward(10)
    sleep(0.5)
    # motor_left.off
    # motor_right.off
    print("Position adjustment finished")
    
def adjust_to_right(motor_left, motor_right):
    
    print("Adjusting position")
    motor_left.Forward(30)
    motor_right.Forward(10)
    sleep(0.5)
    motor_left.Forward(10)
    motor_right.Forward(30)
    sleep(0.5)
    # motor_left.off
    # motor_right.off
    print("Position adjustment finished")