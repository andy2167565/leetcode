class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Reference 1: https://leetcode.com/problems/find-k-closest-elements/solutions/106426/java-c-python-binary-search-o-log-n-k-k/
        # Reference 2: https://leetcode.com/problems/find-k-closest-elements/solutions/462664/python-binary-search-with-detailed-explanation/
        l, r = 0, len(arr) - k
        while l < r:  # Find the starting point of the nearest k elements
            mid = l + (r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:  # x > (arr[mid] + arr[mid + k]) // 2
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]
