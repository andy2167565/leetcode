class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # Reference: https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/solutions/1032070/java-c-python-clean-solution/
        import collections
        m, n = len(a), len(b)
        counter1 = collections.Counter(ord(c) - 97 for c in a)
        counter2 = collections.Counter(ord(c) - 97 for c in b)
        ans = m + n - max((counter1 + counter2).values())  # Condition 3
        for i in range(25):
            counter1[i + 1] += counter1[i]
            counter2[i + 1] += counter2[i]
            ans = min(ans, m - counter1[i] + counter2[i])  # Condition 1
            ans = min(ans, n - counter2[i] + counter1[i])  # Condition 2
        return ans
