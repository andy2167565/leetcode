class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        def backtrack(bag):
            if bag == len(cookies):  # All the bags have been distributed to the children
                return max(distribution)
            unfairness = float('inf')
            for child in range(min(k, bag + 1)):  # Distribute the first (bag + 1) bags to the first (bag + 1) children
                distribution[child] += cookies[bag]  # Assign the cookies in bag to child
                unfairness = min(unfairness, backtrack(bag + 1))
                distribution[child] -= cookies[bag]  # Backtracking
            return unfairness
        return backtrack(0)
