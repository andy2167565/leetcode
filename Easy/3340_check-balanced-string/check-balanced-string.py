class Solution:
    def isBalanced(self, num: str) -> bool:
        arr = list(map(int, num))
        return sum(arr[::2]) == sum(arr[1::2])
