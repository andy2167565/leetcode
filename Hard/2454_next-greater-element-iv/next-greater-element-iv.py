class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/next-greater-element-iv/discuss/2756668/JavaC%2B%2BPython-One-Pass-Stack-Solution-O(n)
        # no_first: index of elements that have not found their first greater element
        # no_second: index of elements that have found their first greater element have not found their second greater element
        ans, no_first, no_second = [-1] * len(nums), [], []
        for i, num in enumerate(nums):
            while no_second and nums[no_second[-1]] < num:  # Found second greater element
                ans[no_second.pop()] = num
            found_first = []
            while no_first and nums[no_first[-1]] < num:  # Found first greater element
                found_first.append(no_first.pop())
            no_second += found_first[::-1]
            no_first.append(i)
        return ans
