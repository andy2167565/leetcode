class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        i, j = sorted((start, destination))
        return min(sum(distance[i:j]), sum(distance[:i] + distance[j:]))
