class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        for i, c in enumerate(sorted(capacity, reverse=True), 1):
            apples -= c
            if apples <= 0:
                return i
