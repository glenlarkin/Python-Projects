import cryptocompare

spike = 'SPIKE'
usd = 'USD'

coinDict = cryptocompare.get_price(spike, usd)
price = coinDict
print(price)