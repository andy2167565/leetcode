class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children  # Give everyone 1 dollar
        if money < 0: return -1  # Do not have enough money to distribute
        ans, r = divmod(money, 7)  # The maximum number of 8's we can distribute
        if ans > children or ans == children and r:  # One of the children gets more than 8 dollars while others get exactly 8 dollars
            return children - 1
        if ans == children - 1 and r == 3:  # One of the children gets 4 dollars while others get exactly 8 dollars
            return children - 2
        return ans
