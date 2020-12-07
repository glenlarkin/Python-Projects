#!python3
# DailyBudget.py - Checks ammount of work and money earned during the day

income = input('How many Hours did you Work Today?\n')
rate = input('How much did you make per hour\n')

total = int(rate) * int(income)
print('Today you made: $' + str(total))
saving = total * 0.15
print('If you save 85%, you may spend: $' + str(saving) + ' today')