class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
#======== <Solution 1> ========#
        x = y = z = 0
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                x, y, z = max(x, a), max(y, b), max(z, c)
        return [x, y, z] == target

#======== <Solution 2> ========#
        x = y = z = False
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                x |= a == target[0]
                y |= b == target[1]
                z |= c == target[2]
            if x and y and z:
                return True
        return False
