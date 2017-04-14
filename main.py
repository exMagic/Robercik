
#Libraries
import RPi.GPIO as GPIO
import time
import tkinter as tk

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
rightRear = GPIO.PWM(36, 100)
GPIO.setup(38, GPIO.OUT)
leftRear = GPIO.PWM(38, 100)

GPIO.setup(35, GPIO.OUT)
rightFront = GPIO.PWM(35, 100)
GPIO.setup(37, GPIO.OUT)
leftFront = GPIO.PWM(37, 100)

def stop():
  rightFront.ChangeDutyCycle(0)
  leftFront.ChangeDutyCycle(0)
  rightRear.ChangeDutyCycle(0)
  leftRear.ChangeDutyCycle(0)
  
def fwd():
  stop()
  rightFront.ChangeDutyCycle(100)
  leftFront.ChangeDutyCycle(100)

def bwd():
  stop()
  rightRear.ChangeDutyCycle(100)
  leftRear.ChangeDutyCycle(100)

def left():
  stop()
  leftFront.ChangeDutyCycle(100)
  rightRear.ChangeDutyCycle(100)
  

def right():
  stop()
  rightFront.ChangeDutyCycle(100)
  leftRear.ChangeDutyCycle(100)
  
rightFront.start(0)                      
leftFront.start(0)
rightRear.start(0)                      
leftRear.start(0)

GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
#GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 18
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        last_time = time.time()
        start_time = time.time()
        bwd()
        left()
        while True:
            dist = distance()
            print ("Masz do przeszkody = %.1f cm" % dist)
            time.sleep(0)
            print('Frame took {} seconds'.format(time.time()-last_time))
            print(start_time)
            print(time.time())
            last_time = time.time()
            if time.time()>start_time+1:
                stop()
                if dist > 40:
                    fwd()
                elif dist <40:
                    bwd()
                    time.sleep(1)
                    left()
                    time.sleep(1)
                    stop()
            
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
