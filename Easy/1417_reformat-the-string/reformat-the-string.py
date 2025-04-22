class Solution:
    def reformat(self, s: str) -> str:
        a, b = '', ''
        for c in s:
            if c.isalpha():
                a += c
            else:
                b += c
        if len(a) < len(b):
            a, b = b, a
        return '' if len(a) - len(b) > 1 else ''.join(a[i // 2] if not i % 2 else b[i // 2] for i in range(len(a) + len(b)))
