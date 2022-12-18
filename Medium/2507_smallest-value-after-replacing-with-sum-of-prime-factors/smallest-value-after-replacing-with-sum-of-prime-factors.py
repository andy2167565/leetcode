class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            curr_sum, curr_n = 0, n
            for i in range(2, n + 1):  # Compute sum of prime factors in current round
                while not curr_n % i:
                    curr_sum += i
                    curr_n //= i
                if curr_n == 1: break  # Early break when there is no more possible factors
            if curr_sum == n: return n  # n is prime or sum of prime factors equals to itself
            n = curr_sum  # Move to next round
