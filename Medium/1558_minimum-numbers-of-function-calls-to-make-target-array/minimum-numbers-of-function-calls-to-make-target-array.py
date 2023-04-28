class Solution:
    def minOperations(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        operations = 0
        while any(nums):
            for i in range(len(nums)):  # Count number of operation 0
                if nums[i] % 2:
                    nums[i] -= 1
                    operations += 1
            if any(nums):  # Count number of operation 1
                for i in range(len(nums)):
                    nums[i] //= 2
                operations += 1
        return operations

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/solutions/805740/java-c-python-bit-counts/
        # (1) The number of operation 0 equals to the total number of bits '1'
        # Count number of odd numbers in the process of making each number 0 by dividing it by 2
        # e.g.   10 ->   5 ->  2 -> 1 -> 0
        #      1010    101    10    1    0
        # There are 2 odd numbers during the process
        # (2) The number of operation 1 equals to maximum bit length - 1
        # Count number of divisions needed to make largest number 0. This is one time task since divisions are shared by all the numbers
        # e.g.   10 ->   5 ->  2 -> 1 -> 0
        #      1010    101    10    1    0
        # There are 4 divisions
        # (3) The total number of operations is 2 + 4 - 1 since making 1 to 0 is common in both steps
        return sum(bin(num).count('1') for num in nums) + len(bin(max(nums))) - 3
