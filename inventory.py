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


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
new_item = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print("Before adding new items")
displayinventory(stuff)
inv = addToInventory(stuff, new_item)
print("\nAfter adding new items")
displayinventory(inv)
