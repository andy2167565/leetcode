class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/avoid-flood-in-the-city/solutions/697950/python-well-explained-simple-logic-o-nlogn-greedy-and-heap/
        import collections, heapq
        ans, rain_days = [-1] * len(rains), collections.defaultdict(list)  # The raining days for each lake in ascending order
        to_empty = []  # The full lakes in the order that will be rained in the most recent future among all other full lakes
        for day, lake in enumerate(rains):
            rain_days[lake].append(day)
        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if rain_days[lake] and rain_days[lake][0] < i:
                    return []
                if rain_days[lake] and len(rain_days[lake]) > 1:
                    heapq.heappush(to_empty, rain_days[lake][1])
            else:
                if to_empty:
                    ans[i] = rains[heapq.heappop(to_empty)]
                    rain_days[ans[i]].pop(0)
                else:
                    ans[i] = 1
        return ans
