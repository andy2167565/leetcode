class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d = {}  # d[i]: The friends that i prefers over his/her partner
        for x, y in pairs:
            d[x] = preferences[x][:preferences[x].index(y)]
            d[y] = preferences[y][:preferences[y].index(x)]
        ans = 0
        for person, friends in d.items():
            for friend in friends:
                if person in d[friend]:  # person and friend are on each other's list
                    ans += 1
                    break
        return ans
