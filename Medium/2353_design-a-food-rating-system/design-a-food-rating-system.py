import collections, heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hashmap = {}
        self.maxHeap = collections.defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.hashmap[food] = (cuisine, rating)
            heapq.heappush(self.maxHeap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.hashmap[food]
        self.hashmap[food] = cuisine, newRating
        heapq.heappush(self.maxHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while -self.maxHeap[cuisine][0][0] != self.hashmap[self.maxHeap[cuisine][0][1]][1]:
            heapq.heappop(self.maxHeap[cuisine])
        return self.maxHeap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
