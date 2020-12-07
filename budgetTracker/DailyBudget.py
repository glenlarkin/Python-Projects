#!python3
# DailyBudget.py - Checks ammount of work and money earned during the day

income = input('How many Hours did you Work Today?\n')
rate = input('How much did you make per hour\n')

result = int(rate) * int(income)
print('Today you made: $' + str(result))