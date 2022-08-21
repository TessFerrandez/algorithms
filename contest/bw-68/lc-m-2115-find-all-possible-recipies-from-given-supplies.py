from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # make supplies a set
        # for each recipe in recipes - make_recipe (if it can be made add it to the supplies)

        supplies = set(supplies)
        recipe_dict = {recipe: ingredient for recipe, ingredient in zip(recipes, ingredients)}
        visited = set()

        def make_ingredient(recipe):
            if recipe in supplies:
                return True
            if recipe not in recipe_dict:
                return False
            # avoid cycle
            if recipe in visited:
                return False
            visited.add(recipe)
            for ingredient in recipe_dict[recipe]:
                if not make_ingredient(ingredient):
                    return False
            supplies.add(recipe)
            return True

        result = []
        for recipe in recipes:
            if make_ingredient(recipe):
                result.append(recipe)

        return result


solution = Solution()
assert solution.findAllRecipes(["ju","fzjnm","x","e","zpmcz","h","q"], [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]], ["f","hveml","cpivl","d"]) == ['ju', 'fzjnm', 'q']
assert solution.findAllRecipes(recipes=["bread"], ingredients=[["yeast","flour"]], supplies=["yeast","flour","corn"]) == ['bread']
assert solution.findAllRecipes(recipes=["bread","sandwich"], ingredients=[["yeast","flour"],["bread","meat"]], supplies=["yeast","flour","meat"]) == ['bread', 'sandwich']
assert solution.findAllRecipes(recipes=["bread","sandwich","burger"], ingredients=[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies=["yeast","flour","meat"]) == ['bread', 'sandwich', 'burger']
