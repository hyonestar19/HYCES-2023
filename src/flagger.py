### THIS FILE GIVES YOU A FLAG
# import
import time

def main(MINUTES, pNAME):
    ## VARIABLE CHECK
    if(type(MINUTES) != int):
        print("MINUTE must set as an integer!!")
        msg = "ERROR: MINUTE doens't correspond with integer type"
        return msg
    
    if(type(pNAME) != str):
        print("pNAME must set as a string")
        msg = "ERROR: pNAME doesn't correspond with string type"
        return msg
    
    ## Calc Minutes
    while(MINUTES != 0):
        MINUTES -= 1
        time.sleep(60)
    
    flag = pNAME + "'s timer is done"
    return flag