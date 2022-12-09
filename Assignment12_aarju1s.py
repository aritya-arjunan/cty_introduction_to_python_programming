def create_file(filename):
    shopping_list = open(filename, 'a+')
    shopping_list.close()

def display_menu(filename):
    print()
    print('This is a shopping list program.')
    print('Here are your options:')
    print('Type 1 to view the list.')
    print('Type 2 to add an item to the list.')
    print('Type 3 to delete an item from the list.')
    print('Type 4 to exit the program.')

    number_input = input('Your choice: ')
    if number_input == '1':
        handle = open(filename, 'r')
        contents = handle.readlines()
        print(contents)
        handle.close()
        display_menu(filename)
    elif number_input == '2':
        item_to_append = input('What would you like to add to the list?\n')
        handle = open(filename, 'a')
        handle.write(item_to_append + '\n')
        handle.close()
        display_menu(filename)
    elif number_input == "3":
        handle = open(filename, 'r')
        item_to_remove = input('What would you like to remove from the '
                                'list (do not include \'\\n\')?\n')
        item_to_remove += '\n'
        contents = handle.readlines()
        if item_to_remove in contents:
            contents.remove(item_to_remove)
            handle = open(filename, 'w')
            handle.writelines(contents)
            handle.close()
        else:
            print('This item is not in the list.')
        display_menu(filename)
    elif number_input == "4":
        return
    else:
        print("Please enter a valid option")
        display_menu(filename)

filename = 'shopping_list.txt'
create_file(filename)
display_menu(filename)
