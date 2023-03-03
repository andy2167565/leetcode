class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Reference: https://leetcode.com/problems/bus-routes/solutions/122771/c-java-python-bfs-solution/
        import collections
        graph = collections.defaultdict(set)  # {stop: set(buses that travel through that stop)}
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
        bfs = [(source, 0)]  # (stop, number of buses taken)
        visited_stop = set([source])
        for stop, count in bfs:
            if stop == target:  # Arrive at target
                return count
            for bus in graph[stop]:  # Travel through routes that include stop
                for next_stop in routes[bus]:
                    if next_stop not in visited_stop:
                        bfs.append((next_stop, count + 1))
                        visited_stop.add(next_stop)
                routes[bus] = []  # Mark route as visited
        return -1
