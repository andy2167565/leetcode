class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
#======== <Solution 1> ========#
        n, seen = len(nums), set()
        for start in range(n):
            divisible, substring = 0, ''
            for num in nums[start:]:
                if not num % p:
                    divisible += 1
                substring += str(num) + ','  # Build the string in CSV format to represent the subarray
                if divisible > k:
                    break
                seen.add(substring)
        return len(seen)

#======== <Solution 2> ========#
        ans, n, trie = 0, len(nums), {}
        for start in range(n):
            curr, divisible = trie, 0
            for num in nums[start:]:
                if not num % p:
                    divisible += 1
                if divisible > k:
                    break
                if num not in curr:
                    curr[num] = {}
                    ans += 1
                curr = curr[num]
        return ans
