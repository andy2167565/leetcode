class Solution:
    def multiply(self, num1: str, num2: str) -> str:
#======== <Solution 1> ========#
        return str(int(num1) * int(num2))

#======== <Solution 2> ========#
        ans = 0
        for i1, n1 in enumerate(reversed(num1)):
            for i2, n2 in enumerate(reversed(num2)):
                ans += int(n1) * 10**i1 * int(n2) *10**i2
        return str(ans)

#======== <Solution 3> ========#
        ans = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans += (ord(num1[len(num1)-1-i]) - ord('0')) * 10**i * (ord(num2[len(num2)-1-j]) - ord('0')) *10**j
        return str(ans)
