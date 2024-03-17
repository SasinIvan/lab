import RPi.GPIO as GPIO

from time import sleep 




def dec2bin(value):
    return [int(element) for element in bin(value) [2:].zfill(8)]

dac =[8, 11, 7, 1, 0, 5, 12, 6] 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

p=1
x=0
try: 
    period = float(input("enter a period of signal: "))

    while True:
        GPIO.output(dac, dec2bin(x))

        if x == 0:
            p =1
        else:
            if x == 25:
                p = 0
        if p == 1:
            x=x+1
            sleep(1)
        else:
            x=x-1
            sleep(1)
        
    

except ValueError:
    print("wrong period!")

finally:
     GPIO.output (dac, 0)
     GPIO.cleanup()

