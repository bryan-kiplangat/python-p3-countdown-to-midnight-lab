#         '''counts down from number and prints "HAPPY NEW YEAR!"'''
import time

def countdown(number):
    while number >= 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        if number == 0:
            print("HAPPY NEW YEAR!")
            break

def countdown_with_sleep(number):
    while number >= 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
        if number == 0:
            print("HAPPY NEW YEAR!")
            break