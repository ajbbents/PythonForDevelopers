# setup for sqlalchamy, creating engine, session, run program
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine("mysql://cf-python:password@localhost/my_database")

Base = declarative_base()

# establishes form of table


class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recpie ID: " + str(self.id) + "-" + self.name + "-" + self.difficulty + ">"

    def __str__(self):
        output = "\nName: " + str(self.name) + \
            "\nCooking time (in mins): " + str(self.cooking_time) + \
            "\nDifficulty: " + str(self.difficulty) + \
            "\nIngredients: " + str(self.ingredients)
        return output


# creates the table in the database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# function to calculate difficulty of recipe


def calculate_difficulty(cooking_time, recipe_ingredients):
    print("Time to calculate_difficulty: ", cooking_time, recipe_ingredients)
    if (cooking_time < 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Easy"
    elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Medium"
    elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Intermediate"
    elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Hard"
    else:
        print("whoops, try that again.")
    print("Difficulty level: ", difficulty_level)
    return difficulty_level

# function to list out all ingredients


def return_ingredients_as_list():
    recipes_list = session.query(Recipe).all()
    for recipe in recipes_list:
        print("Recipe: ", recipe)
        print("recipe.ingredients: ", recipe.ingredients)
        recipe_ingredients_list = recipe.ingredients.split(", ")
        print(recipe_ingredients_list)

# function to create a new recipe


def create_recipe():
    recipe_ingredients = []
    correct_input_name = False
    while correct_input_name == False:
        name = input("\nRecipe name: ")
        if len(name) < 50:
            correct_input_name = True
            correct_input_cooking_time = False
            while correct_input_cooking_time == False:
                cooking_time = input("Cooking time (in mins): ")
                if cooking_time.isnumeric() == True:
                    correct_input_cooking_time = True
                else:
                    print("This one has to be a number.")
        else:
            print("Name is too long - please use less than 50 characters.")
        correct_input_number = False
        while correct_input_number == False:
            ing_nber = input("How many ingredients in your recipe? ")
            if ing_nber.isnumeric() == True:
                correct_input_number = True

                for _ in range(int(ing_nber)):
                    ingredient = input("Enter an ingredient: ")
                    recipe_ingredients.append(ingredient)
            else:
                correct_input_number = False
                print(
                    "Can't be giving ingredients back - please enter a positive number.")
    recipe_ingredients_str = ", ".join(recipe_ingredients)
    print(recipe_ingredients_str)
    difficulty = calculate_difficulty(int(cooking_time), recipe_ingredients)

    recipe_entry = Recipe(
        name=name,
        cooking_time=int(cooking_time),
        ingredients=recipe_ingredients_str,
        difficulty=difficulty
    )

    print(recipe_entry)
    session.add(recipe_entry)
    session.commit()

    print("Thanks for adding your recipe to the database.")

# function to return all recipes


def view_all_recipes():
    all_recipes = []
    all_recipes = session.query(Recipe).all()

    if len(all_recipes) == 0:
        print("No recipes here - don't be hungry, add one!")
        return None
    else:
        print("\nAll recipes: ")
        print("- - - - - - - - - - - - - - - - -")
        for recipe in all_recipes:
            print(recipe)

# function for recipe search by ingredient


def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("Oh man, rough luck. No recipe for that one.")
        return None
    else:
        results = session.query(Recipe.ingredients).all()
        print("Results: ", results)

        all_ingredients = []

        for recipe_ingredients_list in results:
            for recipe_ingredients in recipe_ingredients_list:
                recipe_ingredient_split = recipe_ingredients.split(", ")
                all_ingredients.extend(recipe_ingredient_split)
        print("all_ingredients after loop: ", all_ingredients)

        all_ingredients = list(dict.fromkeys(all_ingredients))
        all_ingredients_list = list(enumerate(all_ingredients))
        print("\nHere are all the ingredients: ")
        print("- - - - - - - - - - - - - - - - -")

        for index, tup in enumerate(all_ingredients_list):
            print(str(tup[0]+1) + ". " + tup[1])

        try:
            ingredient_searched_number = input(
                "\nEnter the number of your chosen ingredient: ")
            ingredient_number_list_searched = ingredient_searched_number.split(
                " ")
            ingredient_searched_list = []
            for ingredient_searched_number in ingredient_number_list_searched:
                ingredient_searched_index = int(ingredient_searched_number) - 1
                ingredient_searched = all_ingredients_list[ingredient_searched_index][1]
                ingredient_searched_list.append(ingredient_searched)
            print("\nYou chose: ", ingredient_searched_list)

            conditions = []
            for ingredient in ingredient_searched_list:
                like_term = "%"+ingredient+"%"
                condition = Recipe.ingredients.like(like_term)
                conditions.append(condition)
            print("conditions: ", conditions)
            searched_recipes = session.query(Recipe).filter(*conditions).all()
            print(searched_recipes)

        except:
            print("Well dang. Something went wrong. Choose a number from the list.")

        else:
            print("searched_recipes: ")
            for recipe in searched_recipes:
                print(recipe)

# function to delete recipe


def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes here - don't be hungry, add one!")
        return None
    else:
        results = session.query(Recipe).with_entities(
            Recipe.id, Recipe.name).all()
        print("results: ", results)
        print("List of available recipes: ")
        for recipe in results:
            print("\nId: ", recipe[0])
            print("Name: ", recipe[1])
        recipe_id_for_deletion = (
            input("\nEnter the ID of the recipe you want gone: "))
        recipe_to_be_deleted = session.query(Recipe).filter(
            Recipe.id == recipe_id_for_deletion).one()
        print("\nWatch it - this one is not coming back: ")
        print(recipe_to_be_deleted)
        deletion_confirmed = input("\nAre you sure? (y or n) ")
        if deletion_confirmed == "y":
            session.delete(recipe_to_be_deleted)
            session.commit()
            print("\nThere it goes. Successfully vanquished.")
        else:
            return None

# function to edit/update recipe


def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes here - don't be hungry, add one!")
        return None
    else:
        results = session.query(Recipe).with_entities(
            Recipe.id, Recipe.name).all()
        print("results: ", results)
        print("List of available recipes: ")
        for recipe in results:
            print("\nId: ", recipe[0])
            print("Name: ", recipe[1])
        recipe_id_for_edit = int(
            input("\nEnter the ID of the recipe you want to edit: "))
        print(session.query(Recipe).with_entities(Recipe.id).all())
        recipes_id_tup_list = session.query(
            Recipe).with_entities(Recipe.id).all()
        recipes_id_list = []
        for recipe_tup in recipes_id_tup_list:
            print(recipe_tup[0])
            recipes_id_list.append(recipe_tup[0])
        print(recipes_id_list)

        if recipe_id_for_edit not in recipes_id_list:
            print("Not in the ID list - try again!")
        else:
            print("Right on. Get to editing!")
            recipe_to_edit = session.query(Recipe).filter(
                Recipe.id == recipe_id_for_edit).one()
            print("\nWatch it - this is the recipe you will modify: ")
            print(recipe_to_edit)
            column_for_update = int(input(
                "\nSelect the number for which one you want to edit: 1. Name, 2. Cooking time, 3. Ingredients"))
            updated_value = (input("\nEnter the new information: "))
            print("Choice: ", updated_value)

            if column_for_update == 1:
                print("Time to update the recipe name: ")
                session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update(
                    {Recipe.name: updated_value})
                session.commit()

            elif column_for_update == 2:
                print("Time to update the cooking time: ")
                session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update(
                    {Recipe.cooking_time: updated_value})
                session.commit()

            elif column_for_update == 3:
                print("Time to update the ingredients: ")
                session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update(
                    {Recipe.ingredients: updated_value})
                session.commit()

            else:
                print("Wrong input, please try again.")
            updated_difficulty = calculate_difficulty(
                recipe_to_edit.cooking_time, recipe_to_edit.ingredients)
            print("updated difficulty: ", updated_difficulty)
            recipe_to_edit.difficulty = updated_difficulty
            session.commit()
            print("Nicely done. All changes made.")

# create main menu.


def main_menu():
    choice = ""
    while (choice != 'quit'):
        print("\n= = = = = = = = = = = = = = =")
        print("\nMain Menu")
        print("- - - - - - - - - -")
        print("Make a choice:")
        print("    1. Create a recipe")
        print("    2. Search for a recipe by ingredient")
        print("    3. Edit a recipe")
        print("    4. Delete a recipe")
        print("    5. View all recipes")
        print("\n    Type 'quit' to exit the program")
        choice = input("\nLet's hear it: ")
        print("\n= = = = = = = = = = = = = = =\n")

        if choice == '1':
            create_recipe()
        elif choice == '2':
            search_by_ingredients()
        elif choice == '3':
            edit_recipe()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            view_all_recipes()
        else:
            if choice == "quit":
                print("See ya!\n")
            else:
                print("Sorry, something is wonky. Try again.")


main_menu()
session.close()
