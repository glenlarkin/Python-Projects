#!/usr/bin/python3

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result

userNumber = input("Give me a number pls: ")

while userNumber != 1:
    userNumber = collatz(int(userNumber))
