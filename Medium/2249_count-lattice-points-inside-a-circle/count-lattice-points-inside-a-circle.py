class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
#======== <Solution 1> ========#
        ans = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (x - i) * (x - i) + (y - j) * (y - j) <= r * r:
                        ans.add((i, j))
        return len(ans)

# Reference: https://leetcode.com/problems/count-lattice-points-inside-a-circle/solutions/1976978/python-explanation-with-pictures-set/
#======== <Solution 2> ========#
        ans = set()
        for x, y, r in circles:
            for dx in range(r + 1):
                for dy in range(r + 1):
                    if dx * dx + dy * dy <= r * r:  # Only need to search for the lattice points in the first quadrant
                        ans.add((x + dx, y + dy))
                        ans.add((x + dx, y - dy))
                        ans.add((x - dx, y + dy))
                        ans.add((x - dx, y - dy))
        return len(ans)

#======== <Solution 3> ========#
        ans = set()
        for x, y, r in circles:
            for dx in range(r + 1):
                y_upper = int((r**2 - dx**2)**0.5)
                for dy in range(y_upper + 1):
                    ans.update([(x + dx, y + dy), (x + dx, y - dy), (x - dx, y + dy), (x - dx, y - dy)])
        return len(ans)
