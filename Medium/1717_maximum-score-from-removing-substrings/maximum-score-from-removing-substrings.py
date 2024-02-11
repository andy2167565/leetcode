class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-score-from-removing-substrings/solutions/1009489/python-c-clean-linear-scan-o-1-space/
        # Proof: https://leetcode.com/problems/maximum-score-from-removing-substrings/solutions/1008908/can-anyone-prove-why-greedy-always-works/
        import collections
        if x < y:  # Ensure the score of ab is always greater than the score of ba
            return self.maximumGain(s[::-1], y, x)
        ans, counter = 0, collections.Counter()
        for c in s + '#':  # Add a character in case that all characters are either a or b at the end
            if c in 'ab':  # Pair as many ab as possible
                if c == 'b' and counter['a']:
                    ans += x
                    counter['a'] -= 1
                else:
                    counter[c] += 1
            else:  # Pair the rest of a's and b's as ba
                ans += min(counter['a'], counter['b']) * y
                counter = collections.Counter()
        return ans
