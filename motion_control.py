from machine import Pin, PWM
from time import sleep

def general_push_button():
    #Set the button pin
    button_pin = 27
    button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)
    bot_state = False
    if button.value() == 1:
        bot_state = True
    return bot_state

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
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    motor_left.Forward(speed)
    motor_right.Forward(speed)
    
def go_back(motor_left, motor_right, speed):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    motor_left.Reverse(speed)
    motor_right.Reverse(speed)

def stop_the_car(motor_left, motor_right):
    # turn a led off when no motors are on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(0)
    
    motor_left.off()
    motor_right.off()

def turn_right_90(motor_left, motor_right):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    print("Turn Right Start")
    speed = 100 # speed subject to adjustment
    motor_left.Forward(speed)
    motor_right.Reverse(speed)
    sleep(0.6) # time subject to adjustment
    motor_left.off()
    motor_right.off()
    led.value(0)
    print("Turn Right Finish")
    
def turn_left_90(motor_left, motor_right):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(10)
    
    print("Trun Left Start")
    speed = 100 # speed subject to adjustment
    motor_left.Reverse(speed)
    motor_right.Forward(speed)
    sleep(0.7) # time subject to adjustment
    motor_left.off()
    motor_right.off()
    led.value(0)
    print("Turn Left Finish")
    
def turn_around(motor_left, motor_right):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    print("Trun Around Start")
    speed = 100 # speed subject to adjustment
    motor_left.Forward(speed)
    motor_right.Reverse(speed)
    sleep(1.2) # time subject to adjustment
    motor_left.off()
    motor_right.off()
    led.value(0)
    print("Turn Around Finish")
    
def adjust_to_right(motor_left, motor_right):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    # After calling this adjustment module, keeping walking straight
    print("Adjusting position to right")
    motor_left.Forward(80)
    motor_right.Forward(40)
    sleep(0.2)
    print("Position adjustment to right finished")
    
def adjust_to_left(motor_left, motor_right):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    # After calling this adjustment module, keeping walking straight
    print("Adjusting position to left")
    motor_left.Forward(40)
    motor_right.Forward(80)
    sleep(0.2)
    print("Position adjustment to left finished")
    
def adjust_to_left_back(motor_left, motor_right):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    # After calling this adjustment module, keeping walking straight
    print("Adjusting position")
    motor_left.Reverse(40)
    motor_right.Reverse(80)
    sleep(0.15)
    print("Position adjustment finished")
    
def adjust_to_right_back(motor_left, motor_right):
    # turn a led on when one motor is on, pin subject to adjustment
    led_pin = 0  # Pin 28 = GP28 (labelled 34 on the jumper)
    led = Pin(led_pin, Pin.OUT)
    led.value(1)
    
    # After calling this adjustment module, keeping walking straight
    print("Adjusting position")
    motor_left.Reverse(80)
    motor_right.Reverse(40)
    sleep(0.15)
    print("Position adjustment finished")