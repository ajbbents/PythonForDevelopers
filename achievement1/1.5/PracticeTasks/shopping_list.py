class ShoppingList(object):
    def __init__(self, list_name):
        shopping_list = []
        self.list_name = list_name
        self.shopping_list = shopping_list

    # add_item checks to see if item is already there, then adds if not
    def add_item(self, item):
        self.item = item
        if (item in self.shopping_list):
            print('this one is already on the list')
        else:
            self.shopping_list.append(item)
            print('got it - added!')

    # remove_item removes item from shopping_list
    def remove_item(self, item):
        self.item = item
        if (item in self.shopping_list):
            self.shopping_list.remove(self.item)
            print('got rid of that one for you.')
        else:
            print('ope, was not there.')

    # prints the contents of self.shopping_list
    def view_list(self):
        print(self.shopping_list)
        print('things on the ' + self.list_name + ': ')
        for item in self.shopping_list:
            print('* ' + item)


# initialize a new list
pet_store_list = ShoppingList('Pet Store List')

# add items to list
pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')

# remove item from list
pet_store_list.remove_item('flea collars')

# attempt adding duplicate item
pet_store_list.add_item('frisbee')

# print entire list
pet_store_list.view_list()
