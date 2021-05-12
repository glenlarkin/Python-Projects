#!/usr/bin/python3
import cryptocompare
usd = 'USD'
ada = 'ADA'

coinbase  = 0
coinbasePro =  0

totalAda = coinbase + coinbasePro

print('you hold ' + str(totalAda) + ' ADA')

def priceFinder():

    coinDict = cryptocompare.get_price(ada, usd)
    price = coinDict[ada][usd]

    for key in coinDict:
        name = key
        
    print('-' *50)
    print('The price of ' + name + ' is currently ' + '$' + str(price))
    print('You own $' + str(totalAda * price) + ' worth of ADA' )
    print('-'*50)

priceFinder()