TRex_loot = ['T-rex tooth', 'car key', 'Park Map',]
inv = {'tokens':42, 'flashlight': 1, 'stun baton': 1}


def display_inventory(inventory): 
    total_items = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k )
        total_items += v
    print()
    print('Total number of items: ' + str(total_items))
    
def add_to_inventory(inventory, added_items):   
    for i in added_items:
        if i in inventory:
            inventory[i] += 1        
        else:
            inventory[i] = 1        
    return inventory

add_to_inventory(inv, TRex_loot)

def main():
    stuff = {'tokens': 42, 'flashlight': 1, 'stun baton': 1}

    TRex_loot = ['T-rex tooth', 'car key', 'Park Map',]

    display_inventory(stuff)

    print('The T-Rex has been chased off Looting...')
    
    print('Inventory Updated!')

    stuff = add_to_inventory(stuff, TRex_loot)

    display_inventory(stuff)

main() #call to main to start executing the code
