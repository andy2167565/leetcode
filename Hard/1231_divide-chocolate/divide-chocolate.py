class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/divide-chocolate/solutions/408503/java-c-python-binary-search/
        l, r = 1, sum(sweetness) // (k + 1)
        while l < r:
            mid = (l + r + 1) // 2
            curr = cuts = 0
            for i in sweetness:
                curr += i
                if curr >= mid:
                    cuts += 1
                    curr = 0
            if cuts > k:
                l = mid
            else:
                r = mid - 1
        return r
