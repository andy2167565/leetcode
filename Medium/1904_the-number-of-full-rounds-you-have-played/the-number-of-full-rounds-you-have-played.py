class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start = int(loginTime[:2]) * 60 + int(loginTime[-2:])
        finish = int(logoutTime[:2]) * 60 + int(logoutTime[-2:])
        if loginTime > logoutTime: finish += 24 * 60
        return max(0, finish // 15 - (start // 15 + (start % 15 > 0)))
