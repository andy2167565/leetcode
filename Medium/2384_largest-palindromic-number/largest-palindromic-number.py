class Solution:
    def largestPalindromic(self, num: str) -> str:
#======== <Solution 1> ========#
        import collections
        counter, half, mid = collections.Counter(num), '', ''
        for digit, count in sorted(counter.items(), reverse=True):
            pairs, single = divmod(count, 2)
            half += pairs * digit  # Add pairs of digits in decreasing order
            mid = max(mid, single * digit)  # Find the maximum digit left if exists
        half = half.lstrip('0')  # Strip the leading zeros
        return half + mid + half[::-1] or '0'  # Return '0' if num consists of even number of zeros e.g. '0000'

#======== <Solution 2> ========#
        import collections
        counter = collections.Counter(num)
        half = ''.join(counter[digit] // 2 * digit for digit in '9876543210').lstrip('0')
        mid = max(counter[digit] % 2 * digit for digit in counter)
        return f'{half}{mid}{half[::-1]}' or '0'
