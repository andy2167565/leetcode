class Solution:
    def bestClosingTime(self, customers: str) -> int:
#======== <Solution 1> ========#
        if 'N' not in customers: return len(customers)
        if 'Y' not in customers: return 0
        ans, idx, penalty = 0, customers.find('N'), float('inf')
        cur = customers[idx:].count('Y')
        for i, ch in enumerate(customers[idx:], idx):
            if cur < penalty:
                ans, penalty = i, cur
            cur += 1 if ch == 'N' else -1
        return len(customers) if cur < penalty else ans

#======== <Solution 2> ========#
        ans = profit = cur = 0
        for i, ch in enumerate(customers):
            cur += (ch == 'Y') * 2 - 1  # Calculate running profit at index i + 1
            if cur > profit:
                ans, profit = i + 1, cur
        return ans

#======== <Solution 3> ========#
        import itertools
        units = [(ch == 'Y') * 2 - 1 for ch in customers]
        profits = list(itertools.accumulate(units, initial=0))
        return profits.index(max(profits))  # Find the first index with maximum profit
