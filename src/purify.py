# import
import gpiozero as gp
import time

# Temporary Variable
TBW = 1 # Notify when the turbin working -> if 1 : Time to work / if 0 : Not yet


# define
def ISFURIFIERWORKING():
    return TBW


# Pin-Setup
TURBIN = gp.DigitalOutputDevice(17)


# Main part of the code
while True:
    if ISFURIFIERWORKING() == 1:
        TURBIN.on()
    else:
        TURBIN.off()
    time.sleep(1)
    print("Iterated\n")