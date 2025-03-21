from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook={}
        for s in supplies:
            can_cook[s]=True
        
        rec_ing = {}
        for i,r in enumerate(recipes):
            rec_ing[r] = i

        
        def dfs(recipe):
            if recipe in can_cook:
                return can_cook[recipe]
            if recipe not in rec_ing:
                return False

            can_cook[recipe]=False
            for n in ingredients[rec_ing[recipe]]:
                if not dfs(n):
                    return False
            can_cook[recipe] = True
            return can_cook[recipe]
            
        res=[]
        for r in recipes:
            if dfs(r):
                res.append(r)
        return res
