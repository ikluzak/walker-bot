import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm_front = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
pwm_back = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
front = servo.Servo(pwm_front)
back  = servo.Servo(pwm_back)

fast = 0.01
slow = 0.1
normal = 0.05

front.angle = 90
back.angle = 90
time.sleep(0.2)

fwd = [60, 100, 100, 100, 100, 60, 60, 60 ]

while True:
    n = 0
    while n < 4:
        front.angle = fwd[2*n]
        back.angle = fwd[(2*n)+1]
        time.sleep(0.3)
        n = n + 1
