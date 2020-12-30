import RPi.GPIO as GPIO
import pigpio
import time

BUTTON_PIN1 = 5
BUTTON_PIN2 = 6
SERVO_PIN1 = 23
SERVO_PIN2 = 24
P_WIDTH = 2500

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def wait_tap(button_pin, servo_pin):
    if GPIO.input(button_pin) == GPIO.HIGH:
        print(button_pin)
        print ("servo set", P_WIDTH )
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(servo_pin, P_WIDTH)
        
        time.sleep(0.5)

        pi.set_servo_pulsewidth(servo_pin, 500)
        time.sleep(1)

try:
    while True:
        wait_tap(button_pin=BUTTON_PIN1, servo_pin=SERVO_PIN1)
        wait_tap(button_pin=BUTTON_PIN2, servo_pin=SERVO_PIN2)

except KeyboardInterrupt:
    pass


GPIO.cleanup()
