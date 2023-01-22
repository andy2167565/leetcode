class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
#======== <Solution 1> ========#
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1

#======== <Solution 2> ========#
        i = 0
        for num in nums1:
            while i < len(nums2) and nums2[i] < num:
                i += 1
            if i < len(nums2) and nums2[i] == num:
                return num
        return -1

#======== <Solution 3> ========#
        for num in nums1:
            l, r = 0, len(nums2) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums2[mid] == num:
                    return num
                elif nums2[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

#======== <Solution 4> ========#
        return min(sorted(set(nums1) & set(nums2)), default=-1)
