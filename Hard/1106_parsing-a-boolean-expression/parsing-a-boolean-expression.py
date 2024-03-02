class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        return eval(expression.replace('t', 'True').replace('f', 'False').replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))
