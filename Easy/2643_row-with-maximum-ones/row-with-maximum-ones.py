class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        i = M = 0
        for j, count in enumerate(map(sum, mat)):
            if count > M:
                i, M = j, count
        return [i, M]
