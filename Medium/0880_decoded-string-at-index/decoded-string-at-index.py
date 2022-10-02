class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # Reference 1: https://leetcode.com/problems/decoded-string-at-index/discuss/156747/JavaC%2B%2BPython-O(N)-Time-O(1)-Space
        # Reference 2: https://leetcode.com/problems/decoded-string-at-index/discuss/979066/Python-O(n)-solution-explained
        i = size = 0
        while size < k:
            if s[i].isdigit():
                size *= int(s[i])
            else:
                size += 1
            i += 1
        for j in reversed(range(i)):
            k %= size
            if s[j].isdigit():
                size //= int(s[j])
            elif not k:
                return s[j]
            else:
                size -= 1
