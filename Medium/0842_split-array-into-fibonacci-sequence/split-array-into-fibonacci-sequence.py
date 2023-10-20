class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def dfs(pos, f=[], x=0):
            if pos == len(num):
                return f if len(f) > 2 else []
            for i in range(pos, len(num)):
                x = x * 10 + int(num[i])
                if x >= 2**31:  # Required only if x < 2**31 to handle overflow
                    break
                if len(f) < 2 or sum(f[-2:]) == x:  # Expand the sequence
                    f.append(x)
                    if dfs(i + 1, f):
                        return f
                    f.pop()  # Backtracking
                if i == pos and num[i] == '0':  # Leading zero
                    break
            return []
        return dfs(0)
