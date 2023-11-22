class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        S, M = sum(milestones), max(milestones)
        return S if S - M >= M else 2 * (S - M) + 1
