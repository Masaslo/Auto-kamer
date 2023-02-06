import RPi.GPIO as GPIO
import time

# Initialize the GPIO library
GPIO.setmode(GPIO.BCM)


# Function to set up the servo on a specific GPIO pin
def servoSetup(pin):
    GPIO.setup(pin, GPIO.OUT)
    return GPIO.PWM(pin, 50)


# Function to set the servo position to a specific angle
def servoWrite(angle, pwm):
    duty = angle / 18 + 2
    pwm.start(duty)
    time.sleep(0.5)
    pwm.stop()
