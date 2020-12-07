#!Python3
# In takes users weekly income, and then creates a daily alotment to spend.

grossPay = input('What was your paycheck before tax?\n')
netPay = input('What was your paycheck after tax?\n')

result =  int(netPay) / int(grossPay)


print(str(result))