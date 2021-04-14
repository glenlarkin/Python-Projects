import cryptocompare

usd = 'USD'


def priceFinder(token, money):
    coinDict = cryptocompare.get_price(token, usd)
    try:
        price = coinDict[token][usd]
    except:
        coinDict = cryptocompare.get_price(token, usd)
        price = coinDict[token][usd]
    
    for key in coinDict:
        name = key
    print('-' *38)
    print('The price of ' + name + ' is currently ' + '$' + str(price))
    print('-'*55)
    print('2x: ' + "{:.2f}".format(price * 2) + ' | 4x: ' + "{:.2f}".format(price * 4) + ' | 6x: ' + "{:.2f}".format(price * 6) + ' | 8x: ' + "{:.2f}".format(price * 8))
    print('10x: ' + "{:.2f}".format(price * 10) + ' | 12x: ' + "{:.2f}".format(price * 12) + ' | 14x: ' + "{:.2f}".format(price * 14) + ' | 16x: ' + "{:.2f}".format(price * 16))
    print('-'*60)
    print('If you invested $' + str(money) )

while True:
    coin = input('What Coin would you like to multiply?\n')
    money = input("How much money will you invest?")
    priceFinder(coin.upper(),int(money))