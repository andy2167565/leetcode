class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i = ans = 0
        pos = dict()  # pos[i]: The last seen position of number i
        for j, num in enumerate(nums):
            temp = pos.copy()
            for k, v in temp.items():
                if abs(k - num) > 2:
                    i = max(i, v + 1)
                    pos.pop(k)
            pos[num] = j
            ans += j - i + 1
        return ans
