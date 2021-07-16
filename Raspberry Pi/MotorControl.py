import RPi.GPIO as GPIO # Import GPIO module
import time # Import time module

ENA = 21
IN1 = 20
IN2 = 16
servoPIN = 2

GPIO.setmode(GPIO.BCM) # Use BCM numbering method
GPIO.setup(ENA, GPIO.OUT) # Set the GPIO pin corresponding to ENA to output mode
GPIO.setup(IN1, GPIO.OUT) # Set the GPIO pin corresponding to IN1 to output mode
GPIO.setup(IN2, GPIO.OUT) # Set the GPIO pin corresponding to IN2 to output mode
GPIO.setup(servoPIN, GPIO.OUT)

freq = 500
speed = 0
pwm = GPIO.PWM(ENA, freq) # Set the input PWM pulse signal to ENA, the frequency is freq and create a PWM object
pwm.start(speed) # Start inputting PWM pulse signal to ENA with the initial duty cycle of speed

# Set the motor to forward rotation
GPIO.output(IN1, False) # Set IN1 to 0
GPIO.output(IN2, True) # Set IN2 to 1
speed = 100
pwm.ChangeDutyCycle(speed)
pwm.ChangeDutyCycle(100)
time.sleep(20)
pwm.stop() # Stop 
GPIO.cleanup() # Clean up and release GPIO resources, reset GPIO

