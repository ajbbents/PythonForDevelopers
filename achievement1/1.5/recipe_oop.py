class Recipe(object):
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.cooking_time = 0
        self.ingredients = []
        self.difficulty = None

    # get name of recipe
    def get_name(self):
        return self.name

    # set name of recipe
    def set_name(self, name):
        self.name = name

    # get cooking time of recipe
    def get_cooking_time(self):
        return self.cooking_time

    # set cooking time of recipe
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # set ingredients for recipe
    def add_ingredients(self, *ingredients):
        self.ingredients = ingredients
        self.update_all_ingredients()

    # get ingredients for recipe
    def get_ingredients(self):
        return self.ingredients

    # create function to calculate recipe difficulty
    def calculate_difficulty(self):
        if (self.cooking_time < 10) and (len(self.ingredients) < 4):
            return 'Easy'
        elif (self.cooking_time < 10) and (len(self.ingredients) >= 4):
            return 'Medium'
        elif (self.cooking_time >= 10) and (len(self.ingredients) < 4):
            return 'Intermediate'
        elif (self.cooking_time >= 10) and (len(self.ingredients) >= 4):
            return 'Hard'
        else:
            print('Well dang, something broke. Try again.')

    # get difficulty level
    def get_difficulty(self):
        if self.difficulty is None:
            self.difficulty = self.calculate_difficulty()
        return self.difficulty

    # ingredient search
    def search_ingredient(self, ingredient, ingredients):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    # create function to check for ingredient currently in list, then add
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    # create recipe search
    def recipe_search(recipes_list, ingredient):
        for recipe in recipes_list:
            if recipe.search_ingredient(ingredient, recipe.ingredients):
                print(recipe)

    def __str__(self):
        output = 'Recipe Name: ' + str(self.name) + \
            '\nCooking time (in mins): ' + str(self.cooking_time) + \
            '\nDifficulty: ' + str(self.difficulty) + \
            '\nIngredients: ' + \
            '\n- - - - - - - -\n'
        for ingredient in self.ingredients:
            output += '* ' + ingredient + '\n'
        return output

    def view_recipe(self):
        print('\nName: ' + str(self.name))
        print('\nCooking time: ' + str(self.cooking_time))
        print('\nDifficulty: ' + str(self.difficulty))
        print('\nIngredients: ')
        show_ingredients = self.get_ingredients()
        for ingredient in show_ingredients:
            print(ingredient)


recipes_list = []

tea = Recipe('Tea')
tea.add_ingredients('Tea leaves', 'Sugar', 'Water')
tea.set_cooking_time(5)
tea.get_difficulty()
recipes_list.append(tea)

coffee = Recipe('Coffee')
coffee.add_ingredients('Ground coffee', 'Sugar', 'Water')
coffee.set_cooking_time(5)
coffee.get_difficulty()
recipes_list.append(coffee)

cake = Recipe('Cake')
cake.add_ingredients('Sugar', 'Butter', 'Eggs',
                     'Vanilla extract', 'Flour', 'Baking powder', 'Milk')
cake.set_cooking_time(50)
cake.get_difficulty()
recipes_list.append(cake)

banana_smoothie = Recipe('Banana Smoothie')
banana_smoothie.add_ingredients(
    'Banana', 'Milk', 'Peanut butter', 'Sugar', 'Ice cubes')
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()
recipes_list.append(banana_smoothie)

print('- - - - - - - - - - -')
print('Recipes list: ')
print('- - - - - - - - - - -')
for recipe in recipes_list:
    print(recipe)

print('Results for recipe_search with water: ')
print('- - -')
Recipe.recipe_search(recipes_list, 'Water')

print('Results for recipe_search with sugar: ')
print('- - -')
Recipe.recipe_search(recipes_list, 'Sugar')

print('Results for recipe_search with banana: ')
print('- - -')
Recipe.recipe_search(recipes_list, 'Banana')
