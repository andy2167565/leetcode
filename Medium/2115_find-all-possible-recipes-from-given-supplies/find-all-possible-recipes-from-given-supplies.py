class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#======== <Solution 1> ========#
        ans, seen, prev_size = [], set(supplies), 0
        while prev_size < len(seen):  # New recipes have been created
            prev_size = len(seen)
            for recipe, items in zip(recipes, ingredients):
                if recipe not in seen and all(item in seen for item in items):  # recipe can be made by existing supplies
                    ans.append(recipe)
                    seen.add(recipe)
        return ans

#======== <Solution 2> ========#
        import collections
        graph, indegrees, q, ans = collections.defaultdict(list), collections.defaultdict(int), collections.deque(supplies), []
        for recipe, items in zip(recipes, ingredients):
            for item in items:
                graph[item].append(recipe)
                indegrees[recipe] += 1
        while q:
            item = q.popleft()
            for recipe in graph[item]:
                indegrees[recipe] -= 1
                if not indegrees[recipe]:  # We have all ingredients required for recipe
                    ans.append(recipe)
                    q.append(recipe)
        return ans
