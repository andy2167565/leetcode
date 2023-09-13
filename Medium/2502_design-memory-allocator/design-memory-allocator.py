import collections
class Allocator:

    def __init__(self, n: int):
        self.memo = [-1] * n
        self.blocks = collections.defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        count = 0  # Count the number of free memory units to be allocated
        for i in range(len(self.memo)):
            if self.memo[i] == -1:
                count += 1
            else:
                count = 0
            if count == size:
                self.memo[i + 1 - count: i + 1] = [mID] * count
                self.blocks[mID].extend(range(i + 1 - count, i + 1))
                return i + 1 - count
        return -1

    def free(self, mID: int) -> int:
        r = len(self.blocks[mID])
        for i in self.blocks[mID]:
            self.memo[i] = -1
        self.blocks[mID] = []
        return r


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
