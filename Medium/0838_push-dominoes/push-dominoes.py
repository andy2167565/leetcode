class Solution:
    def pushDominoes(self, dominoes: str) -> str:
#======== <Solution 1> ========#
        # Reference 1: https://leetcode.com/problems/push-dominoes/solutions/132332/java-c-python-two-pointers/
        # Reference 2: https://leetcode.com/problems/push-dominoes/solutions/1352252/python-simulate-process-explained/
        dominoes = 'L' + dominoes + 'R'  # Add two more dominoes so that we won't miss the edge cases of initial and last postions
        ans, l = '', 0
        for r in range(1, len(dominoes)):
            if dominoes[r] != '.':
                mid = r - l - 1  # The number of dominoes between index l and r
                if l:
                    ans += dominoes[l]
                if dominoes[l] == dominoes[r]:  # 'L...L' or 'R...R': All dominoes are in the same direction
                    ans += dominoes[l] * mid
                elif dominoes[l] == 'L' and dominoes[r] == 'R':  # 'L...R': All dominoes in the middle stay still
                    ans += '.' * mid
                else:  # 'R...L': Fill the first half with 'R' and the second half with 'L', the domino in the middle stays still if exists
                    fall, still = divmod(mid, 2)
                    ans += 'R' * fall + '.' * still + 'L' * fall
                l = r
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/push-dominoes/solutions/2628891/python3-7-lines-with-explanation-t-m-100-98/
        while 'R.' in dominoes or '.L' in dominoes:
            dominoes = dominoes.replace('R.L', '$').replace('R.', 'RR').replace('.L', 'LL')  # Replace 'R.L' with a dummy string first since it remains current state permanently
        return dominoes.replace('$', 'R.L')
