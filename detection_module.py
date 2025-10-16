from machine import Pin, I2C
from utime import sleep
from libs.tiny_code_reader.tiny_code_reader import TinyCodeReader
from libs.VL53L0X.VL53L0X import VL53L0X


def straight_line_detection():
    #Set the LED pin and configuration
    led_pin = 28
    led = Pin(led_pin, Pin.OUT)

    #Set the line sensor pin, sensor 2 and 3 are in the middle, 4 and 1 are offset to left and right respectively
    sensor1_pin = 12
    sensor1 = Pin(sensor1_pin, Pin.IN, Pin.PULL_DOWN)
    sensor2_pin = 12
    sensor2 = Pin(sensor1_pin, Pin.IN, Pin.PULL_DOWN)
    sensor3_pin = 12
    sensor3 = Pin(sensor1_pin, Pin.IN, Pin.PULL_DOWN)
    sensor4_pin = 12
    sensor4 = Pin(sensor1_pin, Pin.IN, Pin.PULL_DOWN)

    #Continiously update the LED value and print said value
    straight = None
    if sensor2.value() == sensor3.value() and sensor1.value() == sensor4.value() and sensor1.value() != sensor2.value():
        led.value(1) # light up the LED if walking in a straight line
        straight = True
    else:
        led.value(0)
        straight = False
    return straight 
        

def qr_code_reader():
    print("Starting tiny code reader...")

    # Set up for the Pico, pin numbers will vary across boards.
    i2c_bus = I2C(id=0, scl=Pin(17), sda=Pin(16), freq=400000) # I2C0 on GP16 & GP17

    i2c_devs = i2c_bus.scan()
    # Uncomment this to see what peripherals were detected on the bus. We would
    # expect to see [12] as the output, since that's the sensor's ID.
    #print(i2c_devs)
    assert len(i2c_devs) == 1 # This demo requires exactly one device
    assert i2c_devs[0] == 12 # Expected device

    tiny_code_reader = TinyCodeReader(i2c_bus)

    print("Polling!")

    # Keep looping and reading the sensor - a real application may do this in
    # a separate thread or a few times when it expects to find a QR code
    code = None
    while code is None:
        sleep(TinyCodeReader.TINY_CODE_READER_DELAY)
        
        code = tiny_code_reader.poll()
        if code is not None:
            print(f"Code found: {code}")
            
    return code

def distance_sensing():
    # config I2C Bus
    i2c_bus = I2C(id=0, sda=Pin(8), scl=Pin(9)) # I2C0 on GP8 & GP9
    # print(i2c_bus.scan())  # Get the address (nb 41=0x29, 82=0x52)
    
    # Setup vl53l0 object
    vl53l0 = VL53L0X(i2c_bus)
    vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[0], 18)
    vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[1], 14)

    print("Starting vl53l0...")

    vl53l0.start()
    distance = vl53l0.read()
    print(f"Distance = {distance}mm")
    vl53l0.stop()
    
    return distance