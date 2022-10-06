class Solution:
    def isNumber(self, s: str) -> bool:
#======== <Solution 1> ========#
        try:
            float(s)
            return s not in ['inf', '+inf', '-inf', 'Infinity', '+Infinity', '-Infinity']
        except:
            return False

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/valid-number/discuss/173977/Python-with-simple-explanation
        dot_seen = e_seen = digit_seen = False
        for i, c in enumerate(s):
            if c.isdigit():
                digit_seen = True
            elif c == '.':
                if e_seen or dot_seen:
                    return False
                dot_seen = True
            elif c in 'eE':
                if e_seen or not digit_seen:
                    return False
                e_seen, digit_seen = True, False
            elif c in '+-':
                if i and s[i - 1] not in 'eE':
                    return False
            else:
                return False
        return digit_seen

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
        # Define DFA state transition tables
        state = [
            # State (0) - initial state
            {'sign': 1, 'digit': 2, '.': 3},
            # State (1) - found sign (expect digit/dot)
            {'digit': 2, '.': 3},
            # State (2) - digit consumer (loop until non-digit)
            {'digit': 2, '.': 4, 'exponent': 5},
            # State (3) - found dot (only a digit is valid)
            {'digit': 4},
            # State (4) - after dot (expect digits, exponent, or end of valid input)
            {'digit': 4, 'exponent': 5},
            # State (5) - found exponent (only a sign or digit valid)
            {'sign': 6, 'digit': 7},
            # State (6) - sign after exponent (only digit)
            {'digit': 7},
            # State (7) - digit after exponent (expect digits or end of valid input)
            {'digit': 7}
        ]
        currentState = 0
        for c in s:
            if c.isdigit():
                c = 'digit'
            elif c in '+-':
                c = 'sign'
            elif c in 'eE':
                c = 'exponent'
            if c not in state[currentState]:
                return False
            currentState = state[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after exponent
        return currentState in [2, 4, 7]

#======== <Solution 4> ========#
        # Reference 1: https://leetcode.com/problems/valid-number/discuss/348874/Python-3-Regex-with-example
        # Reference 2: https://leetcode.com/problems/valid-number/discuss/23910/Simple-one-line-regex-solution
        import re
        return re.match('^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$', s)
