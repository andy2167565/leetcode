class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Reference: https://leetcode.com/problems/reaching-points/solutions/114856/java-c-python-modulo-from-the-end/
        while sx < tx and sy < ty:  # Reduce the target point
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and not (ty - sy) % sx or sy == ty and sx <= tx and not (tx - sx) % sy  # Check if (tx, ty) is equal to (sx, sy + k * sx) or (sx + k * sy, sy)
