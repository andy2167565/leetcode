class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
#======== <Solution 1> ========#
        piles = sorted([a, b, c])
        count = 0
        while piles[1]:
            piles[1] -= 1
            piles[-1] -= 1
            count += 1
            piles.sort()
        return count

#======== <Solution 2> ========#
        a, b, c = sorted([a, b, c])
        count = 0
        while b and a + b > c:
            a -= 1
            b -= 1
            count += 1
        return sum([count, a, b])

#======== <Solution 3> ========#
        a, b, c = sorted([a, b, c])
        return (a + b + c) // 2 if a + b > c else a + b

#======== <Solution 4> ========#
        return min((a + b + c) // 2, a + b + c - max(a, b, c))
