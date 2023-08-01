class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        import collections
        ans, count, hashmap = [], 0, collections.defaultdict(int)
        for i, color in queries:
            if hashmap[i]:  # Update the new color and count
                count -= (hashmap[i - 1] == hashmap[i]) + (hashmap[i + 1] == hashmap[i])
            hashmap[i] = color
            count += (hashmap[i - 1] == hashmap[i]) + (hashmap[i + 1] == hashmap[i])
            ans.append(count)
        return ans
