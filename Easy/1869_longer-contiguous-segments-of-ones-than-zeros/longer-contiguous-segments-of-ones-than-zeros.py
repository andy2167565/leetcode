class Solution:
    def checkZeroOnes(self, s: str) -> bool:
#======== <Solution 1> ========#
        import itertools, operator
        groups = [(g[0], len(list(g[1]))) for g in itertools.groupby(s)]
        num, M = max(groups, key=operator.itemgetter(1))
        return len(set(i for i, l in groups if l == M)) < 2 and int(num)

#======== <Solution 2> ========#
        zeros = ones =  max_zeros = max_ones = 0
        for i in list(map(int, s)):
            if i:
                zeros = 0
                ones += 1
                max_ones = max(max_ones, ones)
            else:
                ones = 0
                zeros += 1
                max_zeros = max(max_zeros, zeros)
        return max_ones > max_zeros

#======== <Solution 3> ========#
        return len(max(s.split('0'))) > len(max(s.split('1')))
