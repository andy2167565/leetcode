class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        import bisect
        arr = []
        for i, num in enumerate(obstacles):
            if not arr or arr[-1] <= num:
                arr.append(num)
                obstacles[i] = len(arr)
            else:
                j = bisect.bisect_right(arr, num)  # Find the index of the smallest number that is larger than num
                arr[j] = num  # Replace that number with num
                obstacles[i] = j + 1
        return obstacles
