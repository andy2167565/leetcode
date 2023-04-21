class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        while i > -1:
            if arr[i] > arr[i + 1]:  # Find the first non-decreasing number from the right
                M = i + 1
                for j in range(M + 1, len(arr)):  # Find the maximum number from numbers at the right side of arr[i] that is smaller than arr[i]
                    if arr[M] < arr[j] < arr[i]:
                        M = j
                arr[i], arr[M] = arr[M], arr[i]
                break
            i -= 1
        return arr
