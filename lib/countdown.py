# your code goes here!
import time

def countdown(n):
    number = n
    while number >= 0:
        if number > 0:
            print(f"{number} SECOND(S)!")
        if number == 0:
            print("HAPPY NEW YEAR!")
        number -= 1
def countdown_with_sleep(n):
    number = n
    while number >= 0:
        if number > 0:
            print(f"{number} SECOND(S)!")
            time.sleep(1)
        if number == 0:
            print("HAPPY NEW YEAR!")
        number -= 1
countdown_with_sleep(10)