#!python3
# DailyBudget.py - Checks amount of work and money earned during the day

income = input('How many Hours did you Work Today?\n')
rate = input('How much did you make per hour\n')

# hourly rate Multiplied by your income
total = int(rate) * int(income)
print('Today you made: $' + str(total))

# Automatically save 15% of earnings
saving = total * 0.15
print('If you save 85%, you may spend: $' + str(saving) + ' today')