class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        ans = bit_any = bit_multi = 0  # bit_any contains all bit 1's that appear in any number, and bit_multi only contains bit 1's that appear in multiple numbers
        for num in nums:
            bit_multi |= num & bit_any
            bit_any |= num
        for num in nums:
            # (1) bit_multi: Bits that appear in multiple numbers
            # (2) bit_any & ~num: Bits that appear in any number that don't appear in current num
            # (3) num << k: Bits we get from LSH of current num by k
            ans = max(ans, bit_multi | bit_any & ~num | num << k)
        return ans
