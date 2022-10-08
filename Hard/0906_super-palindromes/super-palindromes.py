class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/super-palindromes/discuss/174835/tell-you-how-to-get-all-super-palindrome(detailed-explanation)
        left, right = map(int, (left, right))
        ans = sum(left <= i ** 2 <= right for i in range(1, 4))
        for num in range(1, 10000):
            sp = int(str(num) + str(num)[::-1]) ** 2
            if left <= sp <= right and str(sp) == str(sp)[::-1]:
                ans += 1
            for i in range(10):
                sp = int(str(num) + str(i) + str(num)[::-1]) ** 2
                if left <= sp <= right and str(sp) == str(sp)[::-1]:
                    ans += 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/super-palindromes/discuss/170742/Python-super-easy-to-understand-105-complexity-no-cheating
        import math
        left, right = map(int, (left, right))
        n1, n2 = (len(str(math.isqrt(left))) - 1) // 2 + 1, (len(str(math.isqrt(right))) - 1) // 2 + 1
        start, end = 10 ** (n1 - 1), 10 ** n2
        ans = 0
        for i in range(start, end):
            even = int(str(i) + str(i)[::-1])  # e.g. 1221
            odd = int(str(i) + str(i)[:-1][::-1])  # e.g. 121
            for num in [even, odd]:
                sp = num * num
                if left <= sp <= right and str(sp) == str(sp)[::-1]:
                    ans += 1
        return ans
