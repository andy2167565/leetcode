class ATM:

    def __init__(self):
        self.counts = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, count in enumerate(banknotesCount):
            self.counts[i] += count

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in range(4, -1, -1):
            ans[i] = min(self.counts[i], amount // self.values[i])
            amount -= self.values[i] * ans[i]
        if not amount:
            self.deposit([-count for count in ans])
            return ans
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
