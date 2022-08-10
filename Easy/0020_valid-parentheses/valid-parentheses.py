class Solution:
    def isValid(self, s: str) -> bool:
        if len(set(s)) % 2 != 0:
            return False
        else:
            bracket_list = [["(", ")"], ["[", "]"], ["{", "}"]]
            stack = []
            for i in list(s):
                try:
                    if stack:
                        for j in bracket_list:
                            if [stack[-1], i] == j:
                                del stack[-1]
                                raise Exception()
                        stack.append(i)
                    else:
                        stack.append(i)
                except Exception:
                    continue
            return not stack
