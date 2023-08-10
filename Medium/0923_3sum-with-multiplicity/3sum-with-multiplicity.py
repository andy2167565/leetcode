class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # Reference: https://leetcode.com/problems/3sum-with-multiplicity/solutions/181131/c-java-python-o-n-101-101/
        import collections, itertools
        ans, counter = 0, collections.Counter(arr)
        for i, j in itertools.combinations_with_replacement(counter, 2):
            k = target - i - j
            if i == j == k:
                ans += counter[i] * (counter[i] - 1) * (counter[i] - 2) // 6  # n[i]C3
            elif i == j != k:
                ans += counter[i] * (counter[i] - 1) // 2 * counter[k]  # n[i]C2 * n[k]
            elif i < k and j < k:
                ans += counter[i] * counter[j] * counter[k]  # n[i]C1 * n[j]C1 * n[k]C1
        return ans % (10**9 + 7)
