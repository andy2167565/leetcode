class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
#======== <Solution 1> ========#
        return sum(map(ord, coordinates)) % 2

#======== <Solution 2> ========#
        return coordinates[1] in '2468' if coordinates[0] in 'aceg' else coordinates[1] in '1357'
