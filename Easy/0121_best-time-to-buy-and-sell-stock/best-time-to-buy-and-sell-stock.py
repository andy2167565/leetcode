class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#======== <Solution 1> ========#
        min_price, max_profit = prices[0], 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit

#======== <Solution 2> ========#
        max_profit, left = 0, 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit

#======== <Solution 3> ========#
        import operator
        cur_profit, max_profit = 0, 0
        for profit in map(operator.sub, prices[1:], prices):
            cur_profit = max(cur_profit + profit, 0)
            max_profit = max(max_profit, cur_profit)
        return max_profit
