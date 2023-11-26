class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/adding-two-negabinary-numbers/solutions/303751/c-python-convert-from-base-2-addition/
        ans, carry = [], 0
        while arr1 or arr2 or carry:
            carry += (arr1 or [0]).pop() + (arr2 or [0]).pop()
            ans.append(carry & 1)
            carry = -(carry >> 1)
        while len(ans) > 1 and not ans[-1]:
            ans.pop()
        return ans[::-1]
