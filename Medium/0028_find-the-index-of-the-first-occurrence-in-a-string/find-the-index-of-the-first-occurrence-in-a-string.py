class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
#======== <Solution 1> ========#
        hs_id = 0
        while hs_id < len(haystack):
            if haystack[hs_id: hs_id + len(needle)] == needle:
                return hs_id
            hs_id += 1
        return -1

#======== <Solution 2> ========#
        for hs_id in range(len(haystack) - len(needle) + 1):
            if all(haystack[hs_id + nd_id] == needle[nd_id] for nd_id in range(len(needle))):
                return hs_id
        return -1
        
#======== <Solution 3> ========#
        return haystack.index(needle) if needle in haystack else -1

#======== <Solution 4> ========#
        return haystack.find(needle)
