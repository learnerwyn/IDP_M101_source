from machine import Pin, PWM
from utime import sleep

class Forklift:
    def __init__(self, pwm_pin, ground_position = 0, lower_rack_position = 15, raised_position = 30):
        self.pwm = PWM(Pin(pwm_pin), freq=100)
        self.ground_position = ground_position
        self.lower_rack_position = lower_rack_position
        self.raised_position = raised_position
    
    def _updateServo(self, position):
        self.pwm.duty_u16(position)
    
    def goToGroundLevel(self):
        self._updateServo(self.ground_position)
    
    def goToLowerRackLevel(self):
        self._updateServo(self.lower_rack_position)
    
    def goToRaisedLevel(self):
        self._updateServo(self.raised_position)

if __name__ == "__main__":
    forklift = Forklift(15)
    while True:
        forklift.goToGroundLevel()
        sleep(5)
        forklift.goToLowerRackLevel()
        sleep(5)
        forklift.goToRaisedLevel()
        sleep(5)
