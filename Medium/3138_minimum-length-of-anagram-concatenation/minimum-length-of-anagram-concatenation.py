class Solution:
    def minAnagramLength(self, s: str) -> int:
        import collections
        n = len(s)
        for size in range(1, n):  # Iterate over each possible length
            if not n % size:
                base = collections.Counter(s[:size])
                for j in range(size, n, size):
                    if collections.Counter(s[j: j + size]) != base:  # Compare each subsequent substring with the base string
                        break
                else:
                    return size
        return n
