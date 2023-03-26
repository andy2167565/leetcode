class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        isPrime = [False] * 2 + [True] * 999
        for i in range(2, 1001):
            if isPrime[i]:
                for j in range(i * i, 1001, i):
                    isPrime[j] = False
        prev = 0
        for num in nums:
            if prev >= num:  # Still not strictly increasing after subtraction of previous number
                return False
            for i in range(num - 1, -1, -1):
                if isPrime[i] and prev < num - i:  # Pick the largest prime that maintains the strictly increasing order after subtraction
                    break
            prev = num - i
        return True
