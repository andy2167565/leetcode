class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/maximum-good-people-based-on-statements/solutions/1711216/python3-java-c-subsets-o-n-2-2-n/
        def match(seq, pattern):  # Check if person's opinions match the pattern
            return all(str(s) == p for s, p in zip(seq, pattern) if s != 2)  # If the person has no statement skip it instead

        def check(pattern):  # Check if all good people follow the same pattern
            return all(match(statements[i], pattern) for i in range(n) if pattern[i] != '0')

        n, ans = len(statements), 0
        for num in range(1 << n, 1 << (n + 1)):
            permutation = bin(num)[3:]  # Permutation representation of good and bad people in binary
            if check(permutation):  # Check if the permutation satisfies the given constraints
                ans = max(ans, permutation.count('1'))
        return ans
