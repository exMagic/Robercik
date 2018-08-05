import RPi.GPIO as gpio
import time
import sys

gpio.setmode(gpio.BCM)

gpio.setup(6, gpio.OUT)
rightRear = gpio.PWM(6, 100)
gpio.setup(19, gpio.OUT)
leftRear = gpio.PWM(19, 100)

gpio.setup(26, gpio.OUT)
rightFront = gpio.PWM(26, 100)
gpio.setup(13, gpio.OUT)
leftFront = gpio.PWM(13, 100)


def stop():
  rightFront.ChangeDutyCycle(0)
  leftFront.ChangeDutyCycle(0)
  rightRear.ChangeDutyCycle(0)
  leftRear.ChangeDutyCycle(0)
  
def fwd():
  stop()
  rightFront.ChangeDutyCycle(40)
  leftFront.ChangeDutyCycle(40)

def bwd():
  stop()
  rightRear.ChangeDutyCycle(40)
  leftRear.ChangeDutyCycle(40)

def left():
  stop()
  leftFront.ChangeDutyCycle(50)
  rightRear.ChangeDutyCycle(50)
  

def right():
  stop()
  rightFront.ChangeDutyCycle(50)
  leftRear.ChangeDutyCycle(50)
  
rightFront.start(0)                      
leftFront.start(0)
rightRear.start(0)                      
leftRear.start(0)

print('Start')
time.sleep(0.5)
fwd()
time.sleep(0.5)
left()
time.sleep(1.2)
bwd()
time.sleep(0.5)
right()
time.sleep(1.15)


stop()

print('End')
