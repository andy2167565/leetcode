class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import itertools
        m = len(students)
        score = [[0] * m for _ in range(m)]  # score[Student Index][Mentor Index]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))
        return max(sum(score[i][j] for i, j in zip(perm, range(m))) for perm in itertools.permutations(range(m)))

#======== <Solution 2> ========#
        import functools
        m = len(students)
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))
        @functools.cache
        def dfs(mask, j):  # Return max score of assigning students in mask to first j mentors
            ans = 0
            for i in range(m):
                if not mask & (1 << i):
                    ans = max(ans, dfs(mask^(1 << i), j - 1) + score[i][j])
            return ans
        return dfs(1 << m, m - 1)
