class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        import collections
        score = curr = 0
        dq = collections.deque(sorted(tokens))
        while dq and (dq[0] <= power or curr):
            if dq[0] <= power:  # Buy the cheapest token
                power -= dq.popleft()
                curr += 1
            else:  # Sell the most expensive token
                power += dq.pop()
                curr -= 1
            score = max(score, curr)
        return score
