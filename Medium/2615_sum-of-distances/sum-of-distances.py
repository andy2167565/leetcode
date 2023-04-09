class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        import collections
        arr, counter, indices_sum = [0] * len(nums), collections.Counter(nums), collections.defaultdict(int)
        for i, num in enumerate(nums):
            indices_sum[num] += i
        for i, num in enumerate(nums):
            arr[i] = indices_sum[num] - counter[num] * i
            indices_sum[num] -= 2 * i
            counter[num] -= 2
        return arr
        # e.g. nums = [1, 3, 1, 1, 2]
        # indices_sum = {1: 5, 2: 4, 3: 1}
        # counter = {1: 3, 2: 1, 3: 1}
        # Take num = 1 for example:
        # i = 0: arr[0] = |0 - 0| + |2 - 0| + |3 - 0|
        #               = (0 - 0) + (2 - 0) + (3 - 0)
        #               = 5 - 3 * 0
        #               = 5
        # Subtract 2 0's from indices sum and subtract number of 1's by 2(same as adding 2 i's in next round) so that the first term of equation in next round will be positive
        # i = 2: arr[2] = |0 - 2| + |2 - 2| + |3 - 2|
        #               = (2 - 0) + (2 - 2) + (3 - 2)
        #               = 5 - 1 * 2
        #               = 3
        # Subtract 2 2's from indices sum and subtract number of 1's by 2(same as adding 2 i's in next round) so that the second term of equation in next round will be positive
        # i = 3: arr[3] = |0 - 3| + |2 - 3| + |3 - 3|
        #               = (3 - 0) + (3 - 2) + (3 - 3)
        #               = 1 - (-1) * 3
        #               = 4
