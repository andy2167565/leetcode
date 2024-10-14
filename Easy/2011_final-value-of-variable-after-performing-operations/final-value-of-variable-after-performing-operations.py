class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum('+' in s or -1 for s in operations)
