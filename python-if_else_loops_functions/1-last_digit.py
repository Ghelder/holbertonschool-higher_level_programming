#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    ud = number % -10
else:
    ud = number % 10

if ud > 5:
    print(f"Last digit of {number} is {ud} and is greater than 5")
elif ud == 0:
    print(f"Last digit of {number} is {ud} and is 0")
elif ud < 6 and ud != 0:
    print(f"Last digit of {number} is {ud} and is less than 6 and not 0")
