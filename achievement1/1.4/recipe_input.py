import pickle

recipes_list = []
ingredients_list = []

# create difficulty calculation function


def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'hard'

# create recipe input function


def take_recipe():
    name = input("enter recipe name: ")
    cooking_time = int(input("enter cooking time (in mins): "))
    ingredients = input("ingredients (separated by a comma): ").split(", ")
    recipe = {'name': name, 'cooking_time': cooking_time,
              'ingredients': ingredients}
    difficulty = calc_difficulty(recipe)
    return recipe


# open binary file and read, or create one if one doesn't exist
filename = str(input('enter a filename with your recipes: '))
try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print('file not found, creating a new file!')
    data = {'recipes_list': [], 'ingredients_list': []}
except:
    print('some error happened, creating a new file!')
    data = {'recipes_list': [], 'ingredients_list': []}
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    ingredients_list = data['ingredients_list']

# user input for number of recipes (integer)
n = int(input("enter number of recipes: "))

# scans incoming recipe for new ingredients, adds to ingredients_list
for i in range(n):
    recipe = take_recipe()
    print(recipe)

    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

# collects gathered recipes and ingredients
data = {'recipes_list': recipes_list, 'ingredients_list': ingredients_list}

# creates and opens new binary file
new_file_name = str(input('enter a name for your new file, please: '))
new_file_name = open(new_file_name, 'wb')
pickle.dump(data, new_file_name)
