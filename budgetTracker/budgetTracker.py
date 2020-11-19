#!Python3
# In takes users weekly income, and then creates a daily alotment to spend.

def totalPay():
    applePay = int(apple) * 0
    apwPay = int(apw) * 0
    return applePay + apwPay
    
def afterTax():
    appleTax = int(apple) * 0
    apwTax = int(apw) * 0
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
print('You may spend $' + str(daily) + ' each day')
print('You have saved: $' + str(savings))