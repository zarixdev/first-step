inventory = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1, 'strzała': 12}
dragonLoot = ['złote monety', 'jojo', 'sztylet', 'złote monety', 'złote monety', 'ruby', 'Sruby', 'srebro']


def display_inventory(inwentarz):
    przedmioty = 0

    for p, i in inventory.items():
        print(i, p)
        przedmioty += i
    return przedmioty


def addToInventory(inventory, addedItems):
    nowe = {}

    for d in addedItems:
            if d in inventory.keys():
                inventory[d] += 1
            else:
                nowe[d] = 1

    print(nowe)

    inventory = inventory | nowe
    return inventory


inventory = addToInventory(inventory, dragonLoot)
print ('Inwentarz:')
przedmioty = display_inventory(inventory)
print ('Wszystkie przedmioty: ', przedmioty)

