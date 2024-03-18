class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        import collections
        m, n, ans, intensity = len(image), len(image[0]), [], collections.defaultdict(list)

        def isRegion(r, c):
            if r + 3 > m or c + 3 > n:
                return -1
            total = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if i + 1 < r + 3 and abs(image[i][j] - image[i + 1][j]) > threshold:
                        return -1
                    if j + 1 < c + 3 and abs(image[i][j] - image[i][j + 1]) > threshold:
                        return -1
                    total += image[i][j]
            return total // 9
        
        for i in range(m):
            ans.append(image[i][:])
            for j in range(n):
                avg = isRegion(i, j)
                if avg != -1:
                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            intensity[(r, c)].append(avg)
        for i in range(m):
            for j in range(n):
                if intensity[(i, j)]:
                    ans[i][j] = sum(intensity[(i, j)]) // len(intensity[(i, j)])
        return ans
