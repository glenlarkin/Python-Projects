#!/usr/bin/python3

#listToString.py - function that takes a list value as an argument and returns a string of each item separated by commas

spam = ["apple", "banana", "tofu", "cat"]
fruits = ["apple","orange","pear","guava","tomato"]

def listToString(list):
    result = ", ".join(list)
    print(result)
    return(result)
        

listToString(spam)
listToString(fruits)