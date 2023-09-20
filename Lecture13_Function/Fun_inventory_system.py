inventory = []
def Add_inventory():
    item_name = str(input('Enter the item Name: '))
    item_price = int(input('Enter the item Price: '))
    item_quantity = int(input('Enter the item Quantity: '))

    item = (item_name, item_price, item_quantity)
    inventory.append(item)
    print(f'{item[0]} has been added to the inventory')
def Display_inventory():
    if not inventory:
        print('Inventory is empty')
    else:
        print('Current Inventory..')
        for item in inventory:
            print(f'Name: {item[0]} -- Price: {item[1]} -- Quantity: {item[2]}')
def sell_item_inventory():
    global inventory  # Use the global inventory variable

    item_name_to_sell = input('Enter item name to sell: ')
    item_quantity_to_sell = float(input('Enter item quantity which you want to sell: '))

    updated_inventory = []
    item_found = False

    for item in inventory:
        if item[0] == item_name_to_sell:
            if item[2] >= item_quantity_to_sell:
                item = list(item)
                item[2] -= item_quantity_to_sell
                item = tuple(item)
                print(f'{item_quantity_to_sell} {item_name_to_sell} sold.')
                item_found = True
            else:
                print(f'{item_name_to_sell} is out of stock.')
        updated_inventory.append(item)

    if not item_found:
        print(f'{item_name_to_sell} not found in inventory.')

    inventory = updated_inventory  # Update the global inventory list
def Quit_app():
    print('Thanks for using our inventory app..')
while True:
    print('Dashboard')
    print('Press 1 to Add an Inventory')
    print('Press 2 to Display Inventory')
    print('Press 3 to Sell an Item in Inventory')
    print('Press 4 to Quit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        Add_inventory()
    elif choice == 2:
        Display_inventory()
    elif choice == 3:
        sell_item_inventory()
    elif choice == 4:
        Quit_app()
        break
    else:
        print('Invalid Input please choose from given functions')


            
        
        
    
