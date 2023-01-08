class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
#======== <Solution 1> ========#
        l, v, status = 10**4, 10**9, []
        if length >= l or width >= l or height >= l or length * width * height >= v: status.append('Bulky')
        if mass >= 100: status.append('Heavy')
        if len(status) == 2: return 'Both'
        if not status: return 'Neither'
        return status[0]

#======== <Solution 2> ========#
        bulky = max(length, width, height) >= 1e4 or length * width * height >= 1e9
        heavy = mass >= 100
        if bulky and heavy: return 'Both'
        if bulky: return 'Bulky'
        if heavy: return 'Heavy'
        return 'Neither'

#======== <Solution 3> ========#
        idx = int(max(length, width, height) >= 1e4 or length * width * height >= 1e9) + 2 * (mass >= 100)
        return ('Neither', 'Bulky', 'Heavy', 'Both')[idx]
