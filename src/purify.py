# import
import gpiozero as gp

# Variable
TURBIN = gp.DigitalOutputDevice(17)

# MAIN
## Need to give him bool parameter.
def main(ISTURBINWORK):
    ## CHECKING PARAMETER IS CORRECT
    if(type(ISTURBINWORK) != bool):
        print("You give me wrong DATA TYPE!!")
        print("Please check your code!!")
        msg = "ERROR: Wrong Data Type!!"
        
    else:
        if(ISTURBINWORK): # 터빈이 움직여야 할 때
            msg = "Turbin is working for 20 minutes."
            TURBIN.on()
            print("Turbin on!!")
            
        else: # 터빈이 멈출 때
            msg = "Turbin turns off."
            TURBIN.off()
            print("Turbin off!!")

    return msg