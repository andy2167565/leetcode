class Solution:
    def mySqrt(self, x: int) -> int:
#======== <Solution 1> ========#
        return int(sqrt(x))
        
#======== <Solution 2>: Binary Search ========#
        low = 1
        high = x
        while low <= high:
            mid = (low+high) // 2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
