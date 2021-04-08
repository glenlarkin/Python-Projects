#!/usr/bin/python3

# Ethereum Calculator - function that calculates the usd price of Ethereum

import cryptocompare

history = []
end = False

eth = cryptocompare.get_price('ETH', 'USD')
ethPrice = eth['ETH']['USD']


def priceCalc(itemPrice):
    eth = cryptocompare.get_price('ETH', 'USD')
    ethPrice = eth['ETH']['USD']
    total = float(itemPrice) * float(ethPrice)
    print(total)
    history.append(total)

while end != True:
    hello = input('Price of Item: \n')
    priceCalc(hello)
    if hello == 'fuck':
        break