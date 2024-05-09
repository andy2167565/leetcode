class Solution:
    def primePalindrome(self, n: int) -> int:
        # Reference: https://leetcode.com/problems/prime-palindrome/solutions/146798/java-c-python-all-even-length-palindrome-are-divisible-by-11/
        def isPrime(num):
            if num < 2 or not num % 2:
                return num == 2
            return all(num % i for i in range(3, int(num**0.5) + 1, 2))

        if 8 <= n <= 11:
            return 11
        for x in range(10**(len(str(n)) // 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= n and isPrime(y):
                return y
