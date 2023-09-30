class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
# Reference: https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/solutions/1375791/binary-search-derivation-of-formula/
#======== <Solution 1> ========#
        level = apples = 0  # Total number of apples from all the coordinates
        while apples < neededApples:
            level += 1
            apples += 12 * level * level  # Add the apples on the perimeter at each level
        return level * 8

#======== <Solution 2> ========#
        l, r = 1, 100000
        while l < r:
            level = (l + r) // 2
            apples = 2 * level * (level + 1) * (2 * level + 1)
            if apples < neededApples:
                l = level + 1
            else:
                r = level
        return l * 8
