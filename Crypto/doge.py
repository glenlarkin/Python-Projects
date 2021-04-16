import cryptocompare, time, emoji

doge = 'DOGE'
usd = 'USD'
boughtPrice = 0.139

while True:
    print(emoji.emojize("Doge to the Moon :dog:"))
    time.sleep(3)
    
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

    difference = price - boughtPrice
    percent = difference/boughtPrice*100

    if price > boughtPrice:
        print('DogeCoin: ' + str(price) + ' is up! ' + "{:.2f}".format(percent) + ' Percent Gained')
    else:
        print('doge: ' + str(price) + ' is down! ' + "{:.2f}".format(-percent) + ' Percent Lost')
        