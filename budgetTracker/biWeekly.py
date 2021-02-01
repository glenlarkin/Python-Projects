#!Python3
# In takes users weekly income, and then creates a daily alotment to spend.

# Global Variables to be used in both functions
appleRate = 0
apwRate = 0

# Finds Gross pay of both jobs
def totalPay():
    applePay = int(appleHours) * appleRate
    apwPay = int(apwHours) * apwRate
    return applePay + apwPay
    
# Calculates tax into weekly income
def afterTax():
    appleTax = int(appleHours) * appleRate * 0.6
    apwTax = int(apwHours) * apwRate * 0.8
    return appleTax + apwTax 

# Gives user choice of how much they would like to save
saving = input('What Percentage of money would you like to save:  (0.1 = 10%) \n')

# Receive amount of hours worked
appleHours = input('Hours worked the last 2 weeks from Apple: \n')
apwHours = input('Hours worked the last 2 weeks from APW: \n')

# Calulates amount of money saved
savings = afterTax() * float(saving)

# Deducts savings from taxed amount
spendable = afterTax() - savings

# Cutting pay period into weeks, and then into days
daily = spendable / 2 / 7


print('--------------------------------')

print('$' + str(totalPay()) + ' total earned')
print('After Taxes you made: $' + str(afterTax()))
print('If you spend $' + str(daily) + ' each day')
print('You will have saved: $' + str(savings))