class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # Reference: https://leetcode.com/problems/substring-xor-queries/solutions/3174035/hashmap-o-n-30/
        import collections
        seen = collections.defaultdict(lambda: [-1, -1])
        for i, c in enumerate(s):
            val = 0
            for j in range(i, min(i + 30, len(s))):
                val = val * 2 + ord(s[j]) - ord('0')
                if val not in seen:
                    seen[val] = [i, j]
                if c == '0':
                    break
        return [seen[f ^ s] for f, s in queries]
