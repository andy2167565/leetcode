class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/solutions/2038177/python-greedy-prefix-sum-binary-search-easy-to-understand-with-explanation/
        import bisect
        tiles.sort()
        n, startPos = len(tiles), [l for l, _ in tiles]
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + (tiles[i - 1][1] - tiles[i - 1][0] + 1)
        ans = 0
        for i in range(n):
            l, r = tiles[i]
            if r - l >= carpetLen - 1:
                return carpetLen
            endIdx = bisect.bisect_right(startPos, l + carpetLen - 1) - 1  # Binary search the index of the ending tile that the carpet can partially cover
            compensate = 0
            if tiles[endIdx][1] > l + carpetLen - 1:  # Calculate the length of the ending tile that the carpet cannot cover
                compensate = tiles[endIdx][1] - l - carpetLen + 1
            ans = max(ans, preSum[endIdx + 1] - preSum[i] - compensate)
        return ans
