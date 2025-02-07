class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        return sum(colors[i] == colors[(i + 2) % n] != colors[(i + 1) % n] for i in range(n))
