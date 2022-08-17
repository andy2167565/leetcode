class Solution:
    def reachNumber(self, target: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/reach-a-number/discuss/990901/%22Python%22-easy-explanation-blackboard
        target = abs(target)
        step, numMoves = 0, 0
        while step < target or (step - target) % 2:
            numMoves += 1
            step += numMoves
        return numMoves

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/reach-a-number/discuss/990580/Reach-a-Number%3A-Python-O(1)-Time-with-Explanation
        target = abs(target)
        numMoves = ceil(sqrt(2 * target) - 1)
        while True:
            step = numMoves * (numMoves + 1) // 2
            if step >= target and not (step - target) % 2:
                break
            numMoves += 1
        return numMoves

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/reach-a-number/discuss/990399/Python-Math-O(1)-solution-explained
        bound = ceil(sqrt(2 * abs(target) + 0.25) - 0.5)
        if target % 2 == 0:
            if bound % 4 == 1: bound += 2
            if bound % 4 == 2: bound += 1
        else:
            if bound % 4 == 3: bound += 2
            if bound % 4 == 0: bound += 1                
        return bound
