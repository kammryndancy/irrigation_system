# Edit line 6 to match your chosen GPIO pin
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.HIGH)
