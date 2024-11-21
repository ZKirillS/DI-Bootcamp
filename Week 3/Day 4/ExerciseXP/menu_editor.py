from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print('Program Menu')
        print('V - View an item')
        print('A - Add an item')
        print('D - Delete an item')
        print('U - Update an item')
        print('S - Show the menu')
        print('E - Exit')

        user_choise = input('Select an option: ').upper()

        if user_choise == 'V':
            view_item()
        elif user_choise == 'A':
            add_item_to_menu()
        elif user_choise == 'D':
            remove_item_from_menu()
        elif user_choise == 'U':
            update_item_from_menu()
        elif user_choise == 'S':
            show_restaurant_menu()
        elif user_choise == 'E':
            print('Returning to current menu:')
            show_restaurant_menu()
            break
        else:
            print('Invalid choice')


def add_item_to_menu():
    item_name = input('Enter name of item: ')
    try:
        item_price = int(input('Enter the price:'))
        new_item = MenuItem(item_name,item_price)
        new_item.save()
        print(f'{item_name} was added.')
    except ValueError:
        print('Invalid input. Enter a valid integer.')

def remove_item_from_menu():
    item_name = input('Enter item name to remove: ')
    item_to_remove = MenuItem(item_name, 0)
    try:
        item_to_remove.delete()
        print(f'{item_name} was renoved')
    except Exception as exc:
        print(f'Error: {exc}')

def update_item_from_menu():
    item_name = input('Enter name of item to update')
    item = MenuManager.get_by_name(item_name)
    if item:
        print(f'Current item name: {item.item_name}, current price: {item.item_price}')
        new_name = input('Enter new name: ')
        new_price_str = input('Enter new price: ')

        try:
            new_price = int(new_price_str) if new_price_str else item.item_price
            item.update(new_name or item.item_name, new_price)
            print(f'Item "{item_name}" was updated.')
        except ValueError:
            print('Invalid input. Enter a valid integer.')
    else:
        print(f'"{item_name}" not found.')

def view_item():
    item_name = input('Enter name of item to view: ')
    item = MenuManager.get_by_name(item_name)
    if item:
        print(f'Item: {item_name}, Price: ${item.item_price}')
    else:
        print(f'"{item_name}" not found')

def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print('Restaurant Menu')
        for item in items:
            print(f'{item.item_name} - ${item.item_price}')
    else:
        print('No items found')

if __name__ == '__main__':
    show_user_menu()