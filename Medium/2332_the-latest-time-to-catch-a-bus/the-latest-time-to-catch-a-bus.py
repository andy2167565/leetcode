class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        curr_pass = 0
        for time in sorted(buses):
            curr_cap = capacity
            while curr_pass < len(passengers) and passengers[curr_pass] <= time and curr_cap:  # Current passenger gets on the bus
                curr_pass += 1
                curr_cap -= 1
        latest = time if curr_cap else passengers[curr_pass - 1]  # The latest time passengers can catch a bus
        while latest in passengers:
            latest -= 1
        return latest
