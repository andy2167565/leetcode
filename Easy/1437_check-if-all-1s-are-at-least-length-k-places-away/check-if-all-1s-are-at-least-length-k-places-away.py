class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = k
        for num in nums:
            if not num:
                dist += 1
            elif num and dist >= k:
                dist = 0
            else:
                return False
        return True
