class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Reference: https://leetcode.com/problems/maximum-binary-string-after-change/solutions/987335/java-c-python-solution-with-explanation/
        if '0' not in binary:
            return binary
        ones = binary.count('1', binary.find('0'))
        return '1' * (len(binary) - ones - 1) + '0' + '1' * ones
