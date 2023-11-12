class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        import itertools
        offsets = [0] * (len(s) + 1)
        for start, end, direction in shifts:  # The directions are opposite so that only s[start: end + 1] takes effect after accumulation
            offsets[start] += direction * 2 - 1
            offsets[end + 1] -= direction * 2 - 1
        return ''.join((chr((ord(ch) - 97 + offset) % 26 + 97) for ch, offset in zip(s, itertools.accumulate(offsets))))
