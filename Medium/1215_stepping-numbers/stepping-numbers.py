class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
#======== <Solution 1> ========#
        def dfs(num):
            if num <= high:
                if num >= low:
                    nums.add(num)
                digit = num % 10  # Get the last digit of num
                if digit:
                    dfs(num * 10 + digit - 1)  # Append (digit - 1) to num
                if digit < 9:
                    dfs(num * 10 + digit + 1)  # Append (digit + 1) to num
        nums = set()
        for i in range(10):
            dfs(i)
        return sorted(nums)

#======== <Solution 2> ========#
        import collections
        nums, candidates = set(), collections.deque(range(10))
        while candidates:
            num = candidates.popleft()
            if num <= high:
                if num >= low:
                    nums.add(num)
                digit = num % 10
                if digit:
                    candidates.append(num * 10 + digit - 1)
                if digit < 9:
                    candidates.append(num * 10 + digit + 1)
        return sorted(nums)
