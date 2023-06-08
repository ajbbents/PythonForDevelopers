import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='cf-python', passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
    )''')

# define main menu function


def main_menu(conn, cursor):
    choice = ""
    # loop is here, running the main menu
    while (choice != 'quit'):
        print("\n= = = = = = = = = = = = = = =")
        print("\nMain Menu")
        print("- - - - - - - - - -")
        print("Make a choice:")
        print("    1. Create a recipe")
        print("    2. Search for a recipe")
        print("    3. Update a recipe")
        print("    4. Delete a recipe")
        print("    5. View all recipes")
        print("\n    Type 'quit' to exit the program")
        choice = input("\nLet's hear it: ")
        print("\n= = = = = = = = = = = = = = =\n")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            view_all_recipes(conn, cursor)


# define recipe creation function, importing mySQL connection and cursor


def create_recipe(conn, cursor):
    recipe_ingredients = []
    name = str(input("\nRecipe name: "))
    cooking_time = int(input("Cooking time (in mins): "))
    ingredient = input("Ingredients: ")
    recipe_ingredients.append(ingredient)
    difficulty = calculate_difficulty(cooking_time, recipe_ingredients)
    recipe_ingredients_str = ", ".join(recipe_ingredients)
    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, recipe_ingredients_str, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("Thanks for adding your recipe to the database")

# define difficulty calculation function, importing cooking time and ingredients


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

# define recipe search function, importing mySQL connection and cursor


def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    for recipe_ingredients_list in results:
        for recipe_ingredients in recipe_ingredients_list:
            recipe_ingredient_split = recipe_ingredients.split(", ")
            all_ingredients.extend(recipe_ingredient_split)

    all_ingredients = list(dict.fromkeys(all_ingredients))
    all_ingredients_list = list(enumerate(all_ingredients))

    print("\nAll ingredients: ")
    print("- - - - - - - - - -")

    for index, tup in enumerate(all_ingredients_list):
        print(str(tup[0]+1) + ". " + tup[1])

    try:
        ingredient_searched_number = input(
            "\nEnter the number of your chosen ingredient: ")
        ingredient_searched_index = int(ingredient_searched_number) - 1
        ingredient_searched = all_ingredients_list[ingredient_searched_index][1]
        print("\nYou selected: ", ingredient_searched)

    except:
        print("Whoops, something went wrong. Choose a number from the list.")

    else:
        print("\nThe recipe(s) below have your ingredient in them!")
        print("- - - - - - - - - -")
        cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s",
                       ('%' + ingredient_searched + '%', ))

        results_recipes_with_ingredient = cursor.fetchall()
        for row in results_recipes_with_ingredient:
            print("\nID: ", row[0])
            print("Name: ", row[1])
            print("Ingredients: ", row[2])
            print("Cooking time: ", row[3])
            print("Difficulty: ", row[4])

# define recipe update function, importing mySQL connection and cursor


def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_id_for_update = int(
        input("\nEnter the ID for the recipe you want to update: "))
    column_for_update = str(
        input("\nSelect 'name', 'cooking_time' or 'ingredients': "))
    updated_value = input("\nEnter the updated information: ")
    print("Choice: ", updated_value)

    if column_for_update == "name":
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s",
                       (updated_value, recipe_id_for_update))
        print("Recipe updated.")

    elif column_for_update == "cooking_time":
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s",
                       (updated_value, recipe_id_for_update))
        cursor.execute("SELECT * FROM Recipes WHERE id = %s",
                       (recipe_id_for_update, ))
        result_recipe_for_update = cursor.fetchall()
        print("result_recipe_for_update: ", result_recipe_for_update)

        name = result_recipe_for_update[0][1]
        recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
        cooking_time = result_recipe_for_update[0][3]
        updated_difficulty = calculate_difficulty(
            cooking_time, recipe_ingredients)
        print("Updated difficulty: ", updated_difficulty)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s",
                       (updated_difficulty, recipe_id_for_update))
        print("Recipe updated.")

    elif column_for_update == "ingredients":
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s",
                       (updated_value, recipe_id_for_update))
        cursor.execute("SELECT * FROM Recipes WHERE id = %s",
                       (recipe_id_for_update, ))
        result_recipe_for_update = cursor.fetchall()
        print("result_recipe_for_update: ", result_recipe_for_update)

        name = result_recipe_for_update[0][1]
        recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
        cooking_time = result_recipe_for_update[0][3]
        difficulty = result_recipe_for_update[0][4]

        updated_difficulty = calculate_difficulty(
            cooking_time, recipe_ingredients)
        print("Updated difficulty: ", updated_difficulty)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s",
                       (updated_difficulty, recipe_id_for_update))
        print("Recipe updated.")

    conn.commit()

# define recipe delete function, importing mySQL connection and cursor


def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_id_for_deletion = (
        input("\nEnter the ID for the recipe you want gone: "))
    cursor.execute("DELETE FROM Recipes WHERE id = (%s)",
                   (recipe_id_for_deletion, ))
    conn.commit()
    print("\nRecipe has been deleted from the database.")

# define view all recipes function, importing mySQL connection and cursor


def view_all_recipes(conn, cursor):
    print("\nAll recipes: ")
    print("- - - - - - - - - -")
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for row in results:
        print("\nID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking time: ", row[3])
        print("Difficulty: ", row[4])


main_menu(conn, cursor)
print('See ya later!\n')
conn.close()
