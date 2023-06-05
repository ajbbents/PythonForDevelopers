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

    # merge_lists allows more than one list to be combined

    def merge_lists(self, obj):

        # creates name for new merged list
        merged_lists_name = 'merged list: ' + \
            str(self.list_name) + ' and ' + str(obj.list_name)

        # creates an empty ShoppingList object
        merged_lists_obj = ShoppingList(merged_lists_name)

        # adding first list's items to the new list
        merged_lists_obj.shopping_list = self.shopping_list.copy()

        # adding second list's items to new list - checking for redundancies
        for item in obj.shopping_list:
            if not item in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)

        # return new merged list object
        return merged_lists_obj

    # prints the contents of self.shopping_list
    def view_list(self):
        print(self.shopping_list)
        print('things on the ' + self.list_name + ': ')
        for item in self.shopping_list:
            print('* ' + item)


# initialize a new list
pet_store_list = ShoppingList('Pet Store List')

# add items to list
for item in ['dog food', 'collar', 'frisbee', 'bowl']:
    pet_store_list.add_item(item)

# # remove item from list
# pet_store_list.remove_item('flea collars')

# # attempt adding duplicate item
# pet_store_list.add_item('frisbee')

# # print entire list
# pet_store_list.view_list()

# initialize a second list
grocery_store_list = ShoppingList('Grocery Store List')

for item in ['apples', 'bananas', 'beans', 'bowl']:
    grocery_store_list.add_item(item)

merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)
merged_list.view_list()
