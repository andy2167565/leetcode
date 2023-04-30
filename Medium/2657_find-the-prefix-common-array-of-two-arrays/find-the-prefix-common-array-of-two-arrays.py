class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
#======== <Solution 1> ========#
        ans = [int(A[0] == B[0])] + [0] * (len(A) - 1)
        for i, (a, b) in enumerate(zip(A[1:], B[1:]), 1):
            ans[i] = ans[i - 1] + int(a in B[:i + 1]) + int(b in A[:i + 1]) - int(a == b)
        return ans

#======== <Solution 2> ========#
        import collections
        ans, count, counter = [], 0, collections.defaultdict(int)
        for a, b in zip(A, B):
            if a == b:
                count += 1
            else:
                counter[a] += 1
                counter[b] += 1
                count += (counter[a] == 2) + (counter[b] == 2)
            ans.append(count)
        return ans

#======== <Solution 3> ========#
        ans = []
        seen = count = 0
        for pair in zip(A, B):
            for num in pair:
                if (1 << num) & seen:
                    count += 1
                seen |= 1 << num
            ans.append(count)
        return ans
