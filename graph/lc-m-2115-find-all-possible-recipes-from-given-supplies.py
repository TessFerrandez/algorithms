'''
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
'''
from collections import defaultdict
from typing import List


class Solution:
    # stack overflow
    def findAllRecipes2(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        recipie_set = set(recipes)
        recipies_dict = {}
        for i in range(len(recipes)):
            recipies_dict[recipes[i]] = ingredients[i]

        def can_make(ingredient):
            if ingredient in supply_set:
                return True
            elif ingredient in recipie_set:
                for ing in recipies_dict[ingredient]:
                    if not can_make(ing):
                        return False
                supply_set.add(ingredient)
                return True
            else:
                return False

        good = []
        for recipe in recipes:
            if can_make(recipe):
                good.append(recipe)
        return good

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        good_recipes = []
        recipe_ingredients = defaultdict(set)
        ingredient_for = defaultdict(list)

        for i, recipe in enumerate(recipes):
            recipe_ingredients[recipe] = set(ingredients[i])
            for ingredient in ingredients[i]:
                ingredient_for[ingredient].append(recipe)

        while supplies:
            supply = supplies.pop()
            for recipe in ingredient_for[supply]:
                recipe_ingredients[recipe].remove(supply)
                if len(recipe_ingredients[recipe]) == 0:
                    good_recipes.append(recipe)
                    supplies.append(recipe)

        return good_recipes


solution = Solution()

print(solution.findAllRecipes(["ju","fzjnm","x","e","zpmcz","h","q"], [["d"], ["hveml","f","cpivl"], ["cpivl","zpmcz","h","e","fzjnm","ju"], ["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],["f","hveml","cpivl","d"]))
print(solution.findAllRecipes(['bread'], [["yeast","flour"]], ["yeast","flour","corn"]))
print(solution.findAllRecipes(["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]))
print(solution.findAllRecipes(["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]))
print(solution.findAllRecipes(["bread","sandwich","burger", 'vegan'], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"], ["sandwich","meat","bread", 'tomato']], ["yeast","flour","meat"]))
print(solution.findAllRecipes(["bread","sandwich","burger", 'vegan', 'vegan_feast'], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"], ["sandwich","bread",'tomato'], ["vegan","bread"]], ["yeast","flour","meat"]))
