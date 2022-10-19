class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#======== <Solution 1> ========#
        count_dict = {}
        for i in s:
            count_dict[i] = count_dict.get(i, 0) + 1
        for j in t:
            if j not in count_dict:
                return False
            count_dict[j] -= 1
        return all(not val for val in count_dict.values())

#======== <Solution 2> ========#
        return sorted(s) == sorted(t)

#======== <Solution 3> ========#
        import collections
        return collections.Counter(s) == collections.Counter(t)

#======== <Solution 4> ========#
        import string
        return all(s.count(c) == t.count(c) for c in string.ascii_lowercase)
