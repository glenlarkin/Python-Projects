import random
print('I will flip a coin 1000 times. guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads += 1
    flips += 1

    if flips == 900: 
        print('900 flips down and there have been ' + str(heads) + ' heads.')
    if flips == 100:
        print('After 100 tosses, heads has come up ' + str(heads) +  ' times so far')
    if flips == 500:
        print('Halfway there! Update: heads has come up ' + str(heads) + ' times.')

print()
print('Out of 1000 coin tosses, heads came up a total of ' + str(heads) + ' times!')
print('Were you close?')