class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum((ruleKey, ruleValue) in (('type', t), ('color', c), ('name', n)) for t, c, n in items)
