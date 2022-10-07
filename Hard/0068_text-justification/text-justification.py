class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#======== <Solution 1> ========#
        ans, rest, start = [], maxWidth, 0
        for curr, word in enumerate(words):
            if rest - len(word) < curr - start:  # Rest of length for spaces is not enough for current gaps
                if start + 1 == curr:  # Only one word for current line
                    ans.append(words[start].ljust(maxWidth))
                else:
                    s, r = divmod(rest, curr - start - 1)
                    ans.append(''.join(w + ' ' * (s + (k < r)) for k, w in enumerate(words[start: curr - 1])) + words[curr - 1])
                rest, start = maxWidth, curr
            rest -= len(word)
        return ans + [' '.join(words[start:]).ljust(maxWidth)]

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
        ans, line, curr_len = [], [], 0
        for word in words:
            if curr_len + len(word) + len(line) > maxWidth:  # len(line): current number of gaps
                for i in range(maxWidth - curr_len):
                    line[i % (len(line) - 1 or 1)] += ' '
                ans.append(''.join(line))
                line, curr_len = [], 0
            line += [word]
            curr_len += len(word)
        return ans + [' '.join(line).ljust(maxWidth)]
