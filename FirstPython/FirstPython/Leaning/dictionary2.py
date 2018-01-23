def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory

def displayInventory(inventory):
    total_item = 0
    print('Inventory:')
    for key, value in inventory.items():
        total_item += value
        print(str(value) + ' ' + key)
    print('Total items '+ str(total_item))
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
