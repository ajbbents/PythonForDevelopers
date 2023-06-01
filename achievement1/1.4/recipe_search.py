import pickle


# create function to display the recipe
def display_recipe(recipe):
    print('Name: ', recipe['name'])
    print('Cooking time (in mins): ', recipe['cooking_time'])
    print('Ingredients: ', ', '.join(recipe['ingredients']))
    print('Difficulty: ', recipe['difficulty'])


# create function to search ingredient and print all recipes with that ingredient
def search_ingredient(data):
    all_ingredients = data['ingredients_list']
    indexed_all_ingredients = list(enumerate(all_ingredients, 1))

    for ingredient in indexed_all_ingredients:
        print('No.', ingredient[0], ' - ', ingredient[1])
    try:
        chosen_n = int(
            input('enter the corresponding number of your ingredient:   '))
        index = chosen_n - 1
        ingredient_searched = all_ingredients[index]
        ingredient_searched = ingredient_searched.lower()
    except IndexError:
        print('the number you chose is not available')
    except:
        print('an error happened while we were searching')
    else:
        for recipe in data['recipes_list']:
            for recipe_ing in recipe['ingredients']:
                if (recipe_ing == ingredient_searched):
                    print('\nall following recipes include your ingredient: ')
                    display_recipe(recipe)


# file name and storage management with pickle
filename = str(
    input('please enter the filename where you have your recipes stored:  '))
try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print('that file does not exist in the current directory')
    data = {'recipes_list': [], 'ingredients_list': []}
except:
    print('sorry, unexpected error')
    data = {'recipes_list': [], 'ingredients_list': []}
else:
    search_ingredient(data)
finally:
    recipes_file.close()
