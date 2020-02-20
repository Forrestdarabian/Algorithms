#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    ingredient_dict = ingredients
    recipe_dict = recipe

    total = None

    for key in recipe_dict.keys():
        if key not in ingredient_dict:
            return 0
        batches = ingredient_dict[key]//recipe_dict[key]
        if batches == 0:
            return 0

        if not total:
            total = batches
        else:
            total = min(total, batches)

    return total


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
