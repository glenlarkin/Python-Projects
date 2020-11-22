#!python3
"""Separates each word with a comma, Supports multiple lines. 
End by typing a single Period"""
import json
import pyperclip

# Initialize array and variable
wordList = []
context = str

# Loop until a single period is typed
while not (context == '.'):
    context = input('Enter Words that you want to separate by Commas\n')
    # Finds spaces, inserts a comma appropriately
    result = context.replace(' ', ', ')
    wordList.append(result)
    
# Iterate over the list
for i in wordList:
    # Joins the multiple lines together
    print(i, end=', ')