class Solution:
    def maxProduct(self, s: str) -> int:
        n, arr = len(s), []
        for mask in range(1, 1 << n):
            subseq = ''
            for i in range(n):  # Convert the bitmask to the actual subsequence
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:  # Subsequence is palindromic
                arr.append((len(subseq), mask))
        arr.sort(reverse=True)  # Sort by the length of subsequence
        ans = 1
        for i in range(len(arr)):
            len1, mask1 = arr[i]
            if len1**2 < ans:
                break
            for j in range(i + 1, len(arr)):
                len2, mask2 = arr[j]
                if not mask1 & mask2 and len1 * len2 > ans:  # Disjoint
                    ans = len1 * len2
                    break
        return ans
