class Solution:
    def countVowelStrings(self, n: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021493/One-line-solution-or-Math-or-No-DP-no-Big-Integers-or-O(1)-time-space
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24

#======== <Solution 2> ========#
        import math
        return math.comb(n + 4, 4)

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/count-sorted-vowel-strings/discuss/2027353/Python-with-Explanation-(Dynamic-Programming)
        arr = [1, 1, 1, 1, 1]
        for i in range(2, n + 1):
            for j in range(5):
                arr[j] = sum(arr[j:])
        return sum(arr)
