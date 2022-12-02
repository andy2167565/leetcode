class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
#======== <Solution 1> ========#
        import itertools
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return [''.join(i) for i in itertools.product(*[mapping[num] for num in digits])] if digits else []

#======== <Solution 2> ========#
        import functools
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return functools.reduce(lambda acc, digit: [x + y for x in acc for y in mapping[digit]], digits, ['']) if digits else []

#======== <Solution 3> ========#
        if not digits: return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans, stack = [], [(0, '')]
        while stack:
            i, path = stack.pop()
            if i == len(digits):
                ans.append(path)
            else:
                for c in mapping[digits[i]]:
                    stack.append((i + 1, path + c))
        return ans

#======== <Solution 4> ========#
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return self.dfs(mapping, digits, '', []) if digits else []
    
    def dfs(self, mapping, digits, path, ans):
        if digits:
            for c in mapping[digits[0]]:
                self.dfs(mapping, digits[1:], path + c, ans)
        else:
            ans.append(path)
        return ans

#======== <Solution 5> ========#
        if not digits: return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = ['']
        for num in digits:
            ans = [prev + c for prev in ans for c in mapping[num]]
        return ans
