from machine import Pin, PWM
import detection_module
import motion_control

# Alignment procedure to ensure that the robot is properly aligned with the detected line
# If the front sensor does not detect the line, but either left or right sensor does, the robot will adjust its position accordingly.

def align_to_line(motor_left, motor_right):
    
    straight, temp = detection_module.straight_line_detection()
    
    if straight == True:
        print("Aligned with the line.")
    else:
        if temp == "misaligned_to_right":
            print("Bot drifted right. Adjusting position...")
            motion_control.adjust_to_left(motor_left, motor_right)  # Turn left slightly
        elif temp == "misaligned_to_left":
            print("Bot drifted left. Adjusting position...")
            motion_control.adjust_to_right(motor_left, motor_right)  # Turn right slightly
        
def align_to_line_back(motor_left, motor_right):
    # alignment protocol when the bot is going back
    
    straight, temp = detection_module.straight_line_detection()
    
    if straight == True:
        print("Aligned with the line.")
    else:
        if temp == "misaligned_to_right":
            print("Line detected on the left. Adjusting position...")
            motion_control.adjust_to_left_back(motor_left, motor_right)  # Turn left slightly
        elif temp == "misaligned_to_left":
            print("Line detected on the right. Adjusting position...")
            motion_control.adjust_to_right_back(motor_left, motor_right)  # Turn right slightly