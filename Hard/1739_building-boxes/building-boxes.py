class Solution:
    def minimumBoxes(self, n: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/building-boxes/discuss/1032016/C%2B%2B-Python-3-variables-solution-with-drawing-explanation
        cur = floor = layer = box = 0
        while cur < n:
            layer += 1
            floor += layer
            cur += floor
        if cur == n: return floor
        cur -= floor
        floor -= layer
        while cur < n:
            box += 1
            cur += box
        return floor + box

#======== <Solution 2> ========#
        # Reference 1: https://leetcode.com/problems/building-boxes/discuss/1032155/JavaPython-O(1)-Solution
        # Reference 2: https://leetcode.com/problems/building-boxes/discuss/1032104/Python3-math
        # Reference 3: https://en.wikipedia.org/wiki/Tetrahedral_number
        import math
        x = int((6 * n)**(1/3))
        if x * (x + 1) * (x + 2) > 6 * n: x -= 1
        n -= x * (x + 1) * (x + 2) // 6
        return x * (x + 1) // 2 + math.ceil((math.sqrt(1 + 8 * n) - 1) / 2)
