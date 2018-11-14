import RPi.GPIO as gpio
import time

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(18, gpio.OUT)
 
def run(sec):
 init()
 gpio.setup(17, False)
 gpio.setup(18, False)
 time.sleep(sec)
 gpio.cleanup()

print "Executando..."
run(2)
