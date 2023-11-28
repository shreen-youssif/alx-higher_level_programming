#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end= "")
if number > 0:
    digit = number % 10
    if digit == 0:
        print("0")
    elif digit > 6:
        print(f"{digit} is greater than 5")
    else:
        print(f"{digit} is less than 6 and not 0")
else:
    digit = number % -10
    if digit == 0:
        print("0")
    else:
        print(f"{digit} is less than 6 and not 0") 
