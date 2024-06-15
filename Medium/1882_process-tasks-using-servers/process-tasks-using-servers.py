class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/process-tasks-using-servers/solutions/1239767/python-3-simulation-heap-solution/
        import heapq
        ans, free, occupied = [], [[weight, i, 0] for i, weight in enumerate(servers)], []
        heapq.heapify(free)
        for j, task in enumerate(tasks):
            while occupied and occupied[0][0] <= j or not free:
                time, weight, i = heapq.heappop(occupied)  # Release the server with smallest time
                heapq.heappush(free, [weight, i, time])
            weight, i, time = heapq.heappop(free)  # Choose the server with smallest weight and then index
            ans.append(i)
            heapq.heappush(occupied, [max(time, j) + task, weight, i])
        return ans
