class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/campus-bikes-ii/solutions/303422/python-priority-queue/
        import heapq
        def manhattan(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        h, seen = [[0, 0, 0]], set()
        while True:
            dist, worker, taken = heapq.heappop(h)  # Each bit in taken correspond to bike's status: assigned or not
            if (worker, taken) not in seen:
                seen.add((worker, taken))
                if worker == len(workers):
                    return dist
                for bike in range(len(bikes)):
                    if not taken & (1 << bike):
                        heapq.heappush(h, [dist + manhattan(worker, bike), worker + 1, taken | (1 << bike)])
