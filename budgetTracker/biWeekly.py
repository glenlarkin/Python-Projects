#!Python3
# In takes users weekly income, and then creates a daily alotment to spend.

appleRate = 0
apwRate = 0

def totalPay():
    applePay = int(apple) * appleRate
    apwPay = int(apw) * apwRate
    return applePay + apwPay
    
def afterTax():
    appleTax = int(apple) * appleRate * 0.6
    apwTax = int(apw) * apwRate * 0.8
    return appleTax + apwTax 

saving = input('What Percentage of money would you like to save:  (0.1 = 10%) \n')
apple = input('Hours worked the last 2 weeks from Apple: \n')
apw = input('Hours worked the last 2 weeks from APW: \n')

twoWeekTotal = totalPay()
savings = afterTax() * float(saving)

spendable = afterTax() - savings
oneWeek = spendable / 2
daily = oneWeek / 7

print('--------------------------------')

print('$' + str(twoWeekTotal) + ' total earned')
print('After Taxes you made: $' + str(afterTax()))
print('If you spend $' + str(daily) + ' each day')
print('You will have saved: $' + str(savings))