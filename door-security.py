#!/usr/bin env Python3
from gpiozero import Button, OutputDevice
import SimpleMFRC522
import time
import datetime
import logzero
from logzero import logger

relay = OutputDevice(17)
release = Button(27)
reader = SimpleMFRC522.SimpleMFRC522()

relay.on()

logzero.logfile("access.log", maxBytes=1e6, backupCount=3)
def opendoor(id):
        logger.info(id)
        logger.info("The user is "+str(cards[id]))
        relay.off()
        print("DOOR OPEN")
        time.sleep(5)
        relay.on()
        print("DOOR LOCKED")

def button_open():
        logger.info("Door Release Pressed")
        relay.off()
        print("DOOR OPEN")
        time.sleep(5)
        relay.on()
        print("DOOR LOCKED")


#relay.on()
cards = {642581926087: "John Smith",572050203913: "Sarah Rogers"}
while True:
    release.when_pressed = button_open
    time.sleep(0.1)
    id, text = reader.read()
    print(id)
    if id in cards:
        opendoor(id)
    else:
        print("Unknown Card")
        logger.error(id)
        
