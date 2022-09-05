class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
#======== <Solution 1> ========#
        common_prefix = ""
        if strs:
            min_str = min(strs, key=len)
            strs.remove(min_str)
        else:
            return common_prefix
        
        for index, char in enumerate(min_str):
            for word in strs:
                if word[index] != char:
                    return common_prefix
            common_prefix += char
        
        return common_prefix

#======== <Solution 2> ========#
        last = '' if not strs else strs.pop()
        for i, c in enumerate(last):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return last[:i]
        return last

#======== <Solution 3> ========#
        if strs:
            shortest = min(strs, key=len)
            for i, c in enumerate(shortest):
                if any(word[i] != c for word in strs):
                    return shortest[:i]
            return shortest
        return ''

#======== <Solution 4> ========#
        temp, ans = set(), ''
        for i in range(len(min(strs, key=len))):
            for word in strs:
                temp.add(word[i])
            if len(temp) == 1:
                ans += temp.pop()
            else:
                break
        return ans

#======== <Solution 5> ========#
        if not strs:
            return ''
        for i, group in enumerate(zip(*strs)):
            if len(set(group)) > 1:
                return strs[0][:i]
        return min(strs)
