from pyfiglet import Figlet
print('')
text = 'X Calc'
speed = Figlet(font="speed")
print(speed.renderText(text))

multiples = [5, 10, 20, 30, 50, 100]

while True:
    num = input('What number would you like to multiply?\n---------------------------------------\n')
    print('-'*15)
    for x in multiples:
        result = float(num) * x
        print(num + ' X ' + str(x) +' = ' + str(result))
        print('-'*15)