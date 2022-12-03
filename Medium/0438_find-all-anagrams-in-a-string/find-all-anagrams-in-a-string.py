class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
#======== <Solution 1> ========#
        import collections
        ans, target, window = [], collections.Counter(p), collections.Counter(s[:len(p) - 1])
        for i, c in enumerate(s[len(p) - 1:]):
            window[c] += 1  # Add a new char into the window
            if window == target:
                ans.append(i)
            window[s[i]] -= 1  # Decrease the count of oldest char in the window
            if not window[s[i]]:
                del window[s[i]]  # Remove the count if it is 0
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/639309/JavaPython-Sliding-Window-Detail-explanation-Clean-and-Concise
        import collections
        counter_p, ans, l = collections.Counter(p), [], 0
        for r, c in enumerate(s):
            counter_p[c] -= 1
            while counter_p[c] < 0:  # Window contains char c with the number more than in p
                counter_p[s[l]] += 1  # Slide left until counter_p[c] == 0
                l += 1
            if r - l + 1 == len(p):  # Window and p are of equal length
                ans.append(l)
        return ans
