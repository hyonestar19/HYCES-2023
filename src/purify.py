# import
import gpiozero as gp
import time
import random as rd


# Variable
TURBIN = gp.DigitalOutputDevice(17)

    

def main():
    TURBIN.on()
    time.sleep(1)
