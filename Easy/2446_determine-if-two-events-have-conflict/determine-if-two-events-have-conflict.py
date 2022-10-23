class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
#======== <Solution 1> ========#
        # Make sure that event1 always starts before event2
        if event2[0] < event1[0]:
            event1, event2 = event2, event1
        return event2[0] <= event1[1]

# Reference: https://leetcode.com/problems/determine-if-two-events-have-conflict/discuss/2734120/JavaC%2B%2BPython-Easy-1-liner-Solutions
#======== <Solution 2> ========#
        return event1[0] <= event2[1] and event2[0] <= event1[1]

#======== <Solution 3> ========#
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])
