class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
# Reference: https://leetcode.com/problems/k-closest-points-to-origin/discuss/1647773/C%2B%2BPython-Simple-Solutions-w-Explanation-or-Sort-%2B-Heap-%2B-Randomized-QuickSelect-O(N)
#======== <Solution 1> ========#
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]

#======== <Solution 2> ========#
        import heapq
        maxHeap, euclidean = [], lambda x, y: x ** 2 + y ** 2
        for i, (x, y) in enumerate(points):
            heapq.heappush(maxHeap, (-euclidean(x, y), i))  # Negative distance to convert to max-heap (default is min)
            if len(maxHeap) > k:  # Pop the largest element if maxHeap exceeds k elements
                heapq.heappop(maxHeap)
        return [points[i] for _, i in maxHeap]

#======== <Solution 3> ========#
        import heapq
        euclidean = lambda p: p[0] ** 2 + p[1] ** 2
        for p in points:
            p.insert(0, euclidean(p))
        heapq.heapify(points)
        return [heapq.heappop(points)[1:] for _ in range(k)]

#======== <Solution 4> ========#
        import heapq
        return heapq.nsmallest(k, points, lambda p: p[0] ** 2 + p[1] ** 2)

#======== <Solution 5> ========#
        import random
        euclidean = lambda p: p[0] ** 2 + p[1] ** 2
        def partition(L, R):
            rand = random.randint(L, R)  # Choose random pivot
            points[R], points[rand] = points[rand], points[R]  # Swap it to the end
            i, pivotDist = L, euclidean(points[R])
            for j in range(L, R + 1):
                # Move all points with distance less than or equal to pivot to the start
                # pivot is swapped in the last round so that all points on left side of it are definitely less than or equal to it
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            return i - 1  # Return final position of pivot after partition
        L, R, pivot = 0, len(points) - 1, len(points)
        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]

#======== <Solution 6> ========#
        # Reference: https://leetcode.com/problems/k-closest-points-to-origin/discuss/576025/Python-3-lines-kNN-search-using-kd-tree-(for-large-number-of-queries)
        from scipy import spatial
        tree = spatial.KDTree(points)
        # x is the origin, k is the number of closest neighbors, p = 2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=k, p=2)
        return [points[i] for i in idx] if k > 1 else [points[idx]]
