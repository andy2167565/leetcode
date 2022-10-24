class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#======== <Solution 1> ========#
        for c in ransomNote:
            if c not in magazine: return False
            magazine = magazine.replace(c, '', 1)
        return True

#======== <Solution 2> ========#
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))

#======== <Solution 3> ========#
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
