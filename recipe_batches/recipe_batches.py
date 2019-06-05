#!/usr/bin/python

import math


# def recipe_batches(recipe, ingredients):
#     batches = 99999999
#     for ingredient_name, amount_have in ingredients.items():
#         if amount_have - recipe[ingredient_name] >= 0:
#             batches_of_this_ingredient = amount_have // recipe[ingredient_name]
#             if batches_of_this_ingredient < batches:
#                 batches = batches_of_this_ingredient
#         else:
#             batches = 0
#             return batches

#     return batches

def recipe_batches(recipe, ingredients):
    batches = 99999999
    for ingredient_name, amount_required in recipe.items():
        try:
            test = ingredients[ingredient_name]
            if amount_required - ingredients[ingredient_name] <= 0:
                batches_of_this_ingredient = ingredients[ingredient_name] // amount_required
                if batches_of_this_ingredient < batches:
                    batches = batches_of_this_ingredient
            else:
                batches = 0
                return batches
        except KeyError:
            batches = 0
            return batches
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
    ingredients = {'milk': 1288, 'flour': 9, 'sugar': 95}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
