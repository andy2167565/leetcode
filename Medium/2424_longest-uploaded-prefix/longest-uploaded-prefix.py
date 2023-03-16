class LUPrefix:

    def __init__(self, n: int):
        self.prefix = 0
        self.server = set()

    def upload(self, video: int) -> None:
        self.server.add(video)
        while self.prefix + 1 in self.server:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
