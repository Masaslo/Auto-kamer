import wiringpi as wpi
import time

servoPin2 = 23 #fysieke pin is 33
# use 'GPIO naming'
wpi.wiringPiSetup()

# set #1 to be a PWM output

max = 500
min = 75

def servoSetup(servoPin):
    wpi.pinMode(servoPin, wpi.PWM_OUTPUT)
def writeToServo(servoPin, angle):
    write = (((max - min) / 180 ) * angle) + min
    wpi.pwmWrite(servoPin, int(write))
    print(write)
