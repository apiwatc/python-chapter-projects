stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayinventory(inventory):
    print("Inventory")
    total = 0
    for k, v in inventory.items():
        print(k, v)
        total += v
    print("\nTotal of items: " + str(total))


def addToInventory(inventory, addedItem):
    for i in addedItem:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


displayinventory(stuff)
inv = addToInventory(stuff, dragonLoot)

displayinventory(inv)
