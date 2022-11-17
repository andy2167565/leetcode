class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
#======== <Solution 1> ========#
        import itertools
        return list(itertools.permutations(nums))

# Reference: https://leetcode.com/problems/permutations/discuss/2784581/Python-by-list-comprehension-Just-sharing
#======== <Solution 2> ========#
        ans = []
        if not nums:
            ans.append(nums)
        for i, num in enumerate(nums):
            for remain in self.permute(nums[:i] + nums[i + 1:]):  # Permutations of remaining elements
                ans.append([num] + remain)
        return ans

#======== <Solution 3> ========#
        return [[num] + remain for i, num in enumerate(nums) for remain in self.permute(nums[:i] + nums[i + 1:])] or [[]]

# Reference: https://leetcode.com/problems/permutations/discuss/993970/Python-4-Approaches-%3A-Visuals-%2B-Time-Complexity-Analysis
#======== <Solution 4> ========#
        def dfs(nums, path=[], ans=[]):
            if not nums:
                ans.append(path)
            for i, num in enumerate(nums):
                dfs(nums[:i] + nums[i + 1:], path + [num], ans)
            return ans
        return dfs(nums)

#======== <Solution 5> ========#
        def dfs(nums):
            stack, ans = [(nums, [])], []
            while stack:
                nums, path = stack.pop()
                if not nums:
                    ans.append(path)
                for i, num in enumerate(nums):
                    stack.append((nums[:i] + nums[i + 1:], path + [num]))
            return ans
        return dfs(nums)

#======== <Solution 6> ========#
        import collections
        def bfs(nums):
            q, ans = collections.deque([(nums, [])]), []
            while q:
                nums, path = q.popleft()
                if not nums:
                    ans.append(path)
                for i, num in enumerate(nums):
                    q.append((nums[:i] + nums[i + 1:], path + [num]))
            return ans
        return bfs(nums)
