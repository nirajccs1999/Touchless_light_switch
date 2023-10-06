# Import necessary libraries
import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)

# Configure GPIO pins for IR sensors and lighting control
IR_SENSOR_PIN_1 = 17
IR_SENSOR_PIN_2 = 18
LIGHT_CONTROL_PIN = 21

GPIO.setup(IR_SENSOR_PIN_1, GPIO.IN)
GPIO.setup(IR_SENSOR_PIN_2, GPIO.IN)
GPIO.setup(LIGHT_CONTROL_PIN, GPIO.OUT)

IR_THRESHOLD = 1  

def detect_gesture():
    gesture_1 = GPIO.input(IR_SENSOR_PIN_1)
    gesture_2 = GPIO.input(IR_SENSOR_PIN_2)
    
    if gesture_1 == IR_THRESHOLD and gesture_2 == IR_THRESHOLD:
        return "BOTH_COVERED"
    elif gesture_1 == IR_THRESHOLD and gesture_2 != IR_THRESHOLD:
        return "SENSOR_1_COVERED"
    elif gesture_1 != IR_THRESHOLD and gesture_2 == IR_THRESHOLD:
        return "SENSOR_2_COVERED"
    else:
        return "NO_GESTURE"

def control_lights(gesture):
    gesture_1, gesture_2 = gesture
    
    if gesture_1 == IR_THRESHOLD and gesture_2 != IR_THRESHOLD:
        GPIO.output(LIGHT_CONTROL_PIN, GPIO.HIGH)
        print("Lights ON")
    else:
        GPIO.output(LIGHT_CONTROL_PIN, GPIO.LOW)
        print("Lights OFF")

try:
    while True:
        gesture_state = detect_gesture()
        control_lights(gesture_state)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()
