#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_numb = number % 10
else:
    last_numb = number % -10
print("Last digit of {} is ".format(number), end="")

if last_numb > 5:
    print("{} and is greater than 5".format(last_numb))
if last_numb < 6 and last_numb != 0:
    print("{} and is less than 6 and not 0".format(last_numb))
if last_numb == 0:
    print("{} and is 0".format(last_numb))
