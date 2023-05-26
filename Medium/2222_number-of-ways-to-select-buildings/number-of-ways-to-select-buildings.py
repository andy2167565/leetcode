class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {'0': 0, '1': 0, '01': 0, '10': 0, '010': 0, '101': 0}
        for num in s:
            if num == '0':  # Count subsequences ending at current 0
                dp['0'] += 1
                dp['10'] += dp['1']  # The number of 10 depends on how many 1 before current 0
                dp['010'] += dp['01']  # The number of 010 depends on how many 01 before current 0
            else:  # Count subsequences ending at current 1
                dp['1'] += 1
                dp['01'] += dp['0']  # The number of 01 depends on how many 0 before current 1
                dp['101'] += dp['10']  # The number of 101 depends on how many 10 before current 1
        return dp['010'] + dp['101']
