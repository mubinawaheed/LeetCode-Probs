from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToRating = {}
        self.foodToCusine={}
        self.sorted_cuisine_food_map=defaultdict(SortedSet)

        for i in range(len(cuisines)):
           
            self.foodToCusine[foods[i]] = cuisines[i]
            self.sorted_cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))

        for j in range(len(foods)):
            self.foodToRating[foods[j]] = ratings[j]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine_name = self.foodToCusine[food]
        self.sorted_cuisine_food_map[cuisine_name].remove((-self.foodToRating[food], food))
        self.sorted_cuisine_food_map[cuisine_name].add((-newRating, food))
        self.foodToRating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        foods = self.sorted_cuisine_food_map[cuisine]
        return foods[0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)