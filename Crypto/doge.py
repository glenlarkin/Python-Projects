import cryptocompare, time

doge = 'DOGE'
usd = 'USD'

while True:
    query = cryptocompare.get_price(doge, usd)

    
    try:
        price = query[doge][usd]
    except:
        print('error caught')
        query = cryptocompare.get_price(doge, usd)
        
        try: price = query[doge][usd]
        except: 
            if type(price) == None:
                print('now youre really fucked')
                query = cryptocompare.get_price(doge, usd)
    if price < 0.09:
        print('doge: ' + str(price) + ' is less than 9 cents!')
    else:
        print('doge: ' + "{:.3f}".format(price) + ' is more than 9 cents :(')