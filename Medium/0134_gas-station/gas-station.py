class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Reference: https://leetcode.com/problems/gas-station/solutions/860347/python-simple-and-very-short-explained-solution-o-n-o-1-faster-than-98/
        if sum(gas) < sum(cost): return -1  # If sum of gas is not less than sum of cost, there must be a unique solution; otherwise there is no way to get through all stations.
        tank, start, n = 0, 0, len(gas)
        for i in range(n):
            tank += gas[i] - cost[i]
            # If the car cannot travel from A to B, it cannot reach B from any station between A and B either (B is the first station that the car cannot reach from A).
            # Proof: Suppose that the car can travel from C (A < C < B) to B. We can start from A to C and then keep traveling from C to B, which contradicts our precondition.
            if tank < 0:
                start, tank = i + 1, 0
        return start
