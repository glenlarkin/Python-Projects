amount = input('How many DogeCoins do you own?\n')

while True:

    dogePrice = input("When DogeCoin hits : $")

    #amount = 9805.49
    result = float(dogePrice) * float(amount)

    print('I will own: $' + str(result))