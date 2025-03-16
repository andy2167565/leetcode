class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum(all(abs(num1 - num2) > d for num2 in arr2) for num1 in arr1)
