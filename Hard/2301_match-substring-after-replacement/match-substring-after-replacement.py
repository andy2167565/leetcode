class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        import re
        d = {}
        for old, new in mappings:
            d[old] = d.get(old, old) + new
        return bool(re.search(''.join(f'[{d.get(c, c)}]' for c in sub), s))
