# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 1, mountain_arr.length() - 2
        while l < r:  # Find the peak of the mountain
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        l, r = 0, peak
        while l <= r:  # Search the first half of the mountain
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val < target:
                l = mid + 1
            else:
                r = mid - 1
        l, r = peak, mountain_arr.length() - 1
        while l <= r:  # Search the second half of the mountain
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
