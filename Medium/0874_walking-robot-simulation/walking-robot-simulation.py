class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = x = y = 0
        dx, dy = 0, 1  # Face north at the beginning
        obstructionSet = set(map(tuple, obstacles))
        for command in commands:
            if command == -2:  # Turn left
                dx, dy = -dy, dx
            elif command == -1:  # Turn right
                dx, dy = dy, -dx
            else:  # Move forward
                while command and (x + dx, y + dy) not in obstructionSet:
                    x += dx
                    y += dy
                    command -= 1
                ans = max(ans, x * x + y * y)
        return ans
