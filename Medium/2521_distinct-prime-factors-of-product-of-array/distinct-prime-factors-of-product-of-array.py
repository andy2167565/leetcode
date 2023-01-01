class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        def prime_factors(num):
            pfs = set()
            while not num % 2:
                pfs.add(2)
                num //= 2
            for i in range(3, int(num ** 0.5) + 1, 2):
                while not num % i:
                    pfs.add(i)
                    num //= i
            if num > 1:
                pfs.add(num)
            return pfs
        return len(set.union(*[prime_factors(num) for num in nums]))

#======== <Solution 2> ========#
        primes, pfs = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}, set()
        for num in nums:
            for prime in primes:
                while not num % prime:
                    pfs.add(prime)
                    num //= prime
            if num > 1:
                pfs.add(num)
        return len(pfs)
