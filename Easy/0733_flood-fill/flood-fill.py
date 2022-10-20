class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#======== <Solution 1> ========#
        oldColor, m, n = image[sr][sc], len(image), len(image[0])
        if oldColor != color:
            stack = [(sr, sc)]
            while stack:
                i, j = stack.pop()
                image[i][j] = color
                for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= r < m and 0 <= c < n and image[r][c] == oldColor:
                        stack.append((r, c))
        return image

#======== <Solution 2> ========#
        def dfs(i, j):
            image[i][j] = color
            for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= r < m and 0 <= c < n and image[r][c] == oldColor:
                    dfs(r, c)
        oldColor, m, n = image[sr][sc], len(image), len(image[0])
        return (dfs(sr, sc) or image) if oldColor != color else image
