

def addToInventory(inventory, addedItems):
    # Get the first item on the list and add it to the dictionary.
    for lootItem in addedItems:
        # if item doesnt already exist, add it to dictionary
        if lootItem not in inventory.keys():
            inventory[lootItem] = 1
        else:
            # if item exists, increment it by one
            inventory[lootItem] += 1

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
    print('-'*25)

inv = {'gold coin': 42, 'rope': 1}
print('Starting Inventory: ')
displayInventory(inv)

print('You slay a Dragon...')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)


displayInventory(inv)
