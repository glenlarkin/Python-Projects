import cryptocompare

usd = 'USD'
ada = 'ADA'
price = 0

def priceFinder(token):
    coinDict = cryptocompare.get_price(token, usd)
    price = coinDict[token][usd]
    for key in coinDict:
        name = key
    print('-' *50)
    print('The price of ' + name + ' is currently ' + '$' + str(price))
    print('-'*50)
    
priceFinder(ada)

input = input('What coin would you like to check?\n')
priceFinder(input.upper())

while input != 'exit':
    priceFinder(input.upper())
    continue