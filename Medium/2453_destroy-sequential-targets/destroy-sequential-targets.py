class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
#======== <Solution 1> ========#
        target_dict, max_count, ans = {}, 0, float('inf')
        for num in nums:
            base = num % space  # nums[i] = base + c * space => base = nums[i] % space
            target_count, min_target = target_dict.get(base, (0, float('inf')))
            target_dict[base] = (target_count + 1, min(min_target, num))  # Always keep the minimum nums[i] for all targets
            max_count = max(max_count, target_dict[base][0])
        for count, target in target_dict.values():
            if count == max_count:  # Find nums[i] with maximum targets
                ans = min(ans, target)  # If there are more than one nums[i] with equal maximum targets, choose the minimum nums[i]
        return ans

#======== <Solution 2> ========#
        import collections
        counter = collections.Counter(num % space for num in nums)
        max_count = max(counter.values())
        return min(num for num in nums if counter[num % space] == max_count)
