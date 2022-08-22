class Solution:
    def kthFactor(self, n: int, k: int) -> int:
#======== <Solution 1> ========#
        import math
        factors = set()
        for i in range(1, math.isqrt(n) + 1):
            if not n % i:
                factors.update([i, n // i])
        try:
            return sorted(list(factors))[k - 1]
        except:
            return -1

#======== <Solution 2> ========#
        for i in range(1, n + 1):
            if not n % i:
                k -= 1
                if not k:
                    return i
        return -1

#======== <Solution 3> ========#
        count = 0
        for i in range(1, n + 1):
            if not n % i:
                count += 1
                if count == k:
                    return i
        return -1

#======== <Solution 4> ========#
        import math
        for i in range(1, math.isqrt(n) + 1):
            if not n % i:
                k -= 1
                if not k:
                    return i
        if math.isqrt(n) * math.isqrt(n) == n:
            k += 1
        for i in reversed(range(1, math.isqrt(n) + 1)):
            if not n % i:
                k -= 1
                if not k:
                    return n // i
        return -1
