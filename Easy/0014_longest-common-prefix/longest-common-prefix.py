class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        if strs:
            min_str = min(strs, key=len)
            strs.remove(min_str)
        else:
            return common_prefix
        
        for index, char in enumerate(list(min_str)):
            for word in strs:
                if word[index] != char:
                    return common_prefix
            common_prefix += char
        
        return common_prefix
