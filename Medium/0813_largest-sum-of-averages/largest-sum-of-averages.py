class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        scores = {}  # scores[n, k]: The score of partitioning the first n numbers into k groups

        def search(n, k):
            if (n, k) in scores:
                return scores[n, k]
            if n < k:
                return 0
            if k == 1:
                scores[n, k] = sum(nums[:n]) / float(n)
                return scores[n, k]
            curr = scores[n, k] = 0
            for i in range(n - 1, 0, -1):
                curr += nums[i]
                scores[n, k] = max(scores[n, k], search(i, k - 1) + curr / float(n - i))
            return scores[n, k]

        return search(len(nums), k)
