class Bitset:

    def __init__(self, size: int):
        self.bits = [0] * size
        self.ones = 0
        self.flipped = 0

    def fix(self, idx: int) -> None:
        if not (self.bits[idx] ^ self.flipped):
            self.bits[idx] ^= 1
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped:
            self.bits[idx] ^= 1
            self.ones -= 1

    def flip(self) -> None:  # Store the status with a flip flag without actually flipping the bitset
        self.flipped ^= 1
        self.ones = len(self.bits) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.bits)

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(str(i ^ self.flipped) for i in self.bits)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
