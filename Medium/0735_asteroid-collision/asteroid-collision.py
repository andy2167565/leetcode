class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#======== <Solution 1> ========#
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):  # Collision with left < right
                    stack.pop()
                if not stack or stack[-1] < 0:  # num has survived all collisions or asteroids start with some negative values
                    stack.append(num)
                elif stack[-1] == abs(num):  # Collision with the same size
                    stack.pop()
        return stack

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/asteroid-collision/solutions/904475/python-3-stack-simply-clean-o-n-explanation/
        stack = []
        for num in asteroids:
            while stack and stack[-1] > 0 and num < 0:
                if stack[-1] + num < 0:  # Right destroyed left
                    stack.pop()
                elif stack[-1] + num > 0:  # Left destroyed right
                    break
                else:  # Both are destroyed
                    stack.pop()
                    break
            else:  # No collision
                stack.append(num)
        return stack

#======== <Solution 3> ========#
        l, r = 0, 1
        while r < len(asteroids):
            if l < 0 or asteroids[l] < 0 or asteroids[r] > 0:
                # l < 0: Right destroyed left all the way to the start of the stack
                # asteroids[l] < 0: There is no collision whether asteroids[r] is positive or negative
                # asteroids[r] > 0: asteroids[l] > 0 so no collision
                # Ignore nums from asteroids[l + 1] to asteroids[r - 1]
                l += 1
                asteroids[l] = asteroids[r]
                r += 1
            elif asteroids[l] < abs(asteroids[r]):  # Right destroyed left
                l -= 1
            elif asteroids[l] > abs(asteroids[r]):  # Left destroyed right
                r += 1
            else:  # Both are destroyed
                l -= 1
                r += 1
        return asteroids[: l + 1]
