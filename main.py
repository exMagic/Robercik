import RPi.GPIO as gpio
import time
import sys
import paho.mqtt.client as mqtt

gpio.setmode(gpio.BCM)

gpio.setup(6, gpio.OUT)
rightRear = gpio.PWM(6, 100)
gpio.setup(19, gpio.OUT)
leftRear = gpio.PWM(19, 100)

gpio.setup(26, gpio.OUT)
rightFront = gpio.PWM(26, 100)
gpio.setup(13, gpio.OUT)
leftFront = gpio.PWM(13, 100)

rightFront.start(0)                      
leftFront.start(0)
rightRear.start(0)                      
leftRear.start(0)

##########################################################


def stop():
  rightFront.ChangeDutyCycle(0)
  leftFront.ChangeDutyCycle(0)
  rightRear.ChangeDutyCycle(0)
  leftRear.ChangeDutyCycle(0)
  
def fwd( speed ):
  stop()
  rightFront.ChangeDutyCycle( speed )
  leftFront.ChangeDutyCycle( speed )

def bwd( speed ):
  stop()
  rightRear.ChangeDutyCycle( speed )
  leftRear.ChangeDutyCycle( speed )

def left():
  stop()
  leftFront.ChangeDutyCycle(50)
  rightRear.ChangeDutyCycle(50)
  

def right():
  stop()
  rightFront.ChangeDutyCycle(50)
  leftRear.ChangeDutyCycle(50)
##########################################################


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe ("r - 1" ,0 )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "1":
        print("fwd")
        fwd(35)

    if msg.payload == "0":
        print("stop")
        stop()

    if msg.payload == "3":
        print("bwd")
        bwd(35)



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("fbqakwbb", "aHcbcUe7xySu")
client.connect('m20.cloudmqtt.com', 17901, 60)

client.publish ( "r - 1", "start main.py")
client.loop_forever()

#########################################################



  

