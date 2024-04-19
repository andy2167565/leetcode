class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
# Reference: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/solutions/339959/one-pass-o-n-time-and-space/
#======== <Solution 1> ========#
        ans = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            ans += min(arr[i - 1: i] + arr[i + 1: i + 2]) * arr.pop(i)
        return ans

#======== <Solution 2> ========#
        ans, stack = 0, [float('inf')]
        for num in arr:
            while stack[-1] <= num:
                ans += stack.pop() * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        return ans
