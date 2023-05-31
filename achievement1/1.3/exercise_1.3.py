recipes_list = []
ingredients_list = []


def take_recipe():
    name = input("enter recipe name: ")
    cooking_time = int(input("enter cooking time (in mins): "))
    ingredients = input("ingredients (separated by a comma): ").split(", ")
    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    return recipe


n = int(input("enter number of recipes: "))

for i in range(n):
    recipe = take_recipe()
    print(recipe)

    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'hard'

for recipe in recipes_list:
    print('Recipe:', recipe['name'])
    print('Cooking time (in mins):', recipe['cooking_time'])
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty:', recipe['difficulty'])


def print_ingredients():
    ingredients_list.sort()
    print('All ingredients across all recipes')
    print('_______________________')
    for ingredient in ingredients_list:
        print(ingredient)


print_ingredients()
