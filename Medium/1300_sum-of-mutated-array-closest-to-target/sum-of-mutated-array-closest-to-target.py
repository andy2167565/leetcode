class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # Reference: https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/solutions/463306/java-c-python-just-sort-o-nlogn/
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and target >= arr[-1] * len(arr):  # Try value = min(arr) in each round
            target -= arr.pop()  # No need to consider current minimum value in next round
        return round((target - 0.0001) / len(arr)) if arr else max_arr  # If target / len(arr) has 0.5, i.e. there is a tie, we should round down to get the minimum such integer
