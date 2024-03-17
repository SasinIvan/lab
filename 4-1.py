import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def dec2bin(value):
    return [int(element) for element in bin(value) [2:].zfill(8)]

dac =[8, 11, 7, 1, 0, 5, 12, 6] 

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


try:
    while True:
        num =input("put a number from 0-255: ")
        try:
            num=int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                volt = float(num)/(256.0 * 3.3)
                print(f"Output voltage is about{volt:.4}volt")
            else:
                if num <0:
                    print("You entered number < 0!")
                elif num > 255:
                    print("Number is out of range 0-255!")
        except Exception:
                if num =="q": break
                print("You entered a string, not a number 0-255")
finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()
