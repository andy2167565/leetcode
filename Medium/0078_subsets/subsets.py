class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#======== <Solution 1> ========#
        return self.dfs(nums, [])

    def dfs(self, nums, ans, path=[]):
        ans.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], ans, path + [nums[i]])
        return ans

#======== <Solution 2> ========#
        ans = []
        # There are 2 ** len(nums) == 1 << len(nums) combinations
        # Each i in binary format represents whether each element in nums should be included (1) or not (0)
        # e.g. nums = [1, 2, 3], when i = 5 = 101, it indicates the combination [1, 3]
        for i in range(1 << len(nums)):
            path = []
            for j in range(len(nums)):  # Iterate through each binary digit of i
                if i & 1 << j:  # if i >> j & 1:
                    path.append(nums[j])
            ans.append(path)
        return ans

#======== <Solution 3> ========#
        ans = [[]]
        for num in nums:
            ans += [path + [num] for path in ans]
        return ans
