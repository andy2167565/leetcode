class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
#======== <Solution 1> ========#
        if not needle:
            return 0
        
        hs_id = 0
        hs_list = list(haystack)
        nd_list = list(needle)
        while hs_id < len(hs_list):
            try:
                if hs_list[hs_id:hs_id+len(nd_list)] != nd_list:
                    raise Exception
                return hs_id
            except Exception:
                hs_id += 1
        return -1
        
#======== <Solution 2> ========#
        for hs_id in range(len(haystack) - len(needle) + 1):
            if all(haystack[hs_id+nd_id] == needle[nd_id] for nd_id in range(len(needle))):
                return hs_id
        return -1
        
#======== <Solution 3> ========#
        try:
            return haystack.index(needle)
        except:
            return -1
