class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        return [num for num in set(nums) if nums.count(num) > len(nums) // 3]

#======== <Solution 2> ========#
        # Reference 1: https://leetcode.com/problems/majority-element-ii/discuss/63502/6-lines-general-case-O(N)-time-and-O(k)-space
        # Reference 2: https://leetcode.com/problems/majority-element-ii/discuss/858872/Python-Voting-O(n)-solution-explained
        import collections
        counter = collections.Counter()
        for num in nums:
            counter[num] += 1
            if len(counter) == 3:
                counter -= collections.Counter(counter.keys())
        return [num for num in counter if nums.count(num) > len(nums) // 3]
