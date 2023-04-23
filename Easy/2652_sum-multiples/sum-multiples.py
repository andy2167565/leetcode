class Solution:
    def sumOfMultiples(self, n: int) -> int:
#======== <Solution 1> ========#
        return sum(num for num in range(1, n + 1) if not num % 3 or not num % 5 or not num % 7)

#======== <Solution 2> ========#
        fn = lambda x: x * (n // x) * (n // x + 1) // 2  # Sum of multiples of x
        return fn(3) + fn(5) + fn(7) - fn(15) - fn(21) - fn(35) + fn(105)
