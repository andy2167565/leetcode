class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [float('inf')] * n  # dp[i]: Height for first i books
        for i in range(1, n + 1):
            w, h, j = 0, 0, i - 1  # Open a new row for book (i - 1)
            while j >= 0 and w + books[j][0] <= shelfWidth:  # Place as many books in the row as possible starting from book (i - 1)
                h = max(h, books[j][1])
                w += books[j][0]
                dp[i] = min(dp[i], dp[j] + h)  # Update current height for first i books
                j -= 1
        return dp[-1]
