import RPi.GPIO as gpio
import time
 
def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(18, gpio.OUT)
 
def run(sec):
 init()
 gpio.output(17, True)
 gpio.output(18, True)
 time.sleep(sec)
 gpio.cleanup()
 
print("Running...")
run(2)
print("Finished...")

