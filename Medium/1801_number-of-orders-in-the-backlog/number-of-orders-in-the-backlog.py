class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        import heapq
        sell, buy = [], []
        for price, amount, orderType in orders:
            if not orderType:
                heapq.heappush(buy, [-price, amount])  # max heap
            else:
                heapq.heappush(sell, [price, amount])  # min heap
            while sell and buy and sell[0][0] <= -buy[0][0]:
                deal = min(buy[0][1], sell[0][1])
                buy[0][1] -= deal
                sell[0][1] -= deal
                if not buy[0][1]:
                    heapq.heappop(buy)
                if not sell[0][1]:
                    heapq.heappop(sell)
        return sum(amount for _, amount in buy + sell) % (10**9 + 7)
