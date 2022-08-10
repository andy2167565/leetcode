class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#======== <Solution 1> ========#
        while nums2:
            nums1.append(nums2[-1])
            nums1.remove(0)
            del nums2[-1]
        nums1.sort()
        
#======== <Solution 2> ========#
        nums1[m:] = nums2
        nums1.sort()
        
#======== <Solution 3> ========#
        i = m + n - 1
        m -= 1
        n -= 1
        # Scan both lists from the end and take larger one
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
        # All elements in nums1 have been sorted and placed from the end
        # Put remaining elements in nums2 into the head of nums1
        if m < 0:
            nums1[:i+1] = nums2[:n+1]
