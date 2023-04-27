class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import collections
        reserved_groups = collections.defaultdict(set)
        for row, seat in reservedSeats:
            if seat in [2, 3, 4, 5]:  # The first four-person group has been occupied
                reserved_groups[row].add(0)
            if seat in [4, 5, 6, 7]:  # The second four-person group has been occupied
                reserved_groups[row].add(1)
            if seat in [6, 7, 8, 9]:  # The third four-person group has been occupied
                reserved_groups[row].add(2)
        return 2 * n - sum(1 + (len(groups) == 3) for groups in reserved_groups.values())
        # (1) No group is occupied: We can assign a maximum of 2 groups
        # (2) 1 or 2 groups are occupied: Only 1 empty group left
        # (3) All 3 groups are occupied: No empty group for assignment

#======== <Solution 2> ========#
        import collections
        reserved_seats = collections.defaultdict(set)
        for row, seat in reservedSeats:
            reserved_seats[row].add(seat)
        ans = 2 * (n - len(reserved_seats))
        for group in reserved_seats.values():
            if not group & {2, 3, 4, 5} or not group & {4, 5, 6, 7} or not group & {6, 7, 8, 9}:
                ans += 1
            if not group & {2, 3, 4, 5, 6, 7, 8, 9}:
                ans += 1
        return ans
