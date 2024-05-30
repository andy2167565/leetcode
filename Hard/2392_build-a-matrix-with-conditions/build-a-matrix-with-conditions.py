class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Reference: https://leetcode.com/problems/build-a-matrix-with-conditions/solutions/2492947/python-3-explanation-with-pictures-topological-sort/
        import collections

        def helper(conditions):
            nxt, indegree = [set() for _ in range(k)], [0] * k
            for i, j in set(tuple(arr) for arr in conditions):  # Convert conditions into a set of tuples
                nxt[i - 1].add(j - 1)
                indegree[j - 1] += 1

            ans, dq = [], collections.deque(i for i in range(k) if not indegree[i])
            while dq:
                curr = dq.popleft()
                ans.append(curr)
                for cand in nxt[curr]:
                    indegree[cand] -= 1
                    if not indegree[cand]:
                        dq.append(cand)
            return ans if len(ans) == k else []

        ans1, ans2 = helper(rowConditions), helper(colConditions)
        if not ans1 or not ans2:
            return []

        arr = [[0] * k for _ in range(k)]
        for i in range(k):
            arr[ans1.index(i)][ans2.index(i)] = i + 1
        return arr
