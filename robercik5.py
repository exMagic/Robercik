#first comment in this code:)

import RPi.GPIO as GPIO
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
print(3)
def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

    if key_press == 'up':
      fwd()
	  
    elif key_press == 'down':
      bwd()
    elif key_press == 'left':
      left()
    elif key_press == 'right':
      right()
    elif key_press == 'space':
      stop()
      

command = tk.Tk()
command.bind_all('<Key>', key_input)
command.mainloop()


