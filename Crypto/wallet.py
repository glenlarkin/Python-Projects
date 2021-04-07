import cryptocompare
import json

usd = 'USD'
total = 0.0
totalMoney = 0.0

btc = {'name':'BTC', 'amount':0.00424593, 'price': 58_000}
eth = {'name':'ETH', 'amount':0.0095, 'price': 1800}
ada = {'name':'ADA', 'amount': 169.443295, 'price':1.21}
storj = {'name':'STORJ', 'amount':67.75069148, 'price': 2.97}
bch = {'name':'BCH', 'amount': 0.07585611, 'price': 600}
ogn = {'name':'OGN', 'amount':167.23311362, 'price':1.72}
spi = {'name':'SPI', 'amount':0.938, 'price': 241}
chain = {'name':'CHAIN', 'amount': 215.144, 'price':0.725292}

wallet = [btc, eth, ada, storj, bch, ogn, spi, chain]

# Original purchase price
for coin in wallet:
    purchase = coin['amount'] * coin['price']
    total += purchase
    print(coin['name'] + ' was bought for: $' + str(purchase))
print(str(total) + ' Has been spent on Crypto')

# Current Worth
for coin in wallet:
    crypto = cryptocompare.get_price(coin['name'], usd)
    price = crypto[coin['name']][usd]
    worth = coin['amount'] * price
    print('You own $' + str(worth) + ' of ' + coin['name'])
    totalMoney += worth
print(totalMoney)    
difference = totalMoney - total

if difference > 0:
    print('You have made $' + str(difference) + '\nDoge Coin To the Moon!!!')
elif difference == 0:
    print('Hold your breath and hope that it goes up!')
else:
    print('You have lost $' + str(difference) + '\nI hope I never see this message!!!') 