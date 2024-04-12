class Solution:
    def numberOfWays(self, corridor: str) -> int:
# Reference: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/solutions/1709725/java-c-python-two-solutions-with-explanation/
#======== <Solution 1> ========#
        ans, seats = 1, [i for i, c in enumerate(corridor) if c == 'S']
        for i in range(1, len(seats) - 1, 2):
            ans *= seats[i + 1] - seats[i]
        return ans % (10**9 + 7) * (not len(seats) % 2 and len(seats) >= 2)

#======== <Solution 2> ========#
        zero_seat, one_seat, two_seats = 1, 0, 0
        for c in corridor:
            if c == 'S':
                zero_seat, one_seat, two_seats = 0, zero_seat + two_seats, one_seat
            else:
                zero_seat += two_seats
        return two_seats % (10**9 + 7)
