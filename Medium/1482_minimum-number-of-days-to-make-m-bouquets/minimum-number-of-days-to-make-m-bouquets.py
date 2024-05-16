class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            flower = bouquet = 0
            for day in bloomDay:
                flower = 0 if day > mid else flower + 1  # Collect the adjacent flowers that will bloom within mid days
                if flower >= k:  # Make a bouquet with collected flowers
                    flower = 0
                    bouquet += 1
                    if bouquet == m:
                        break
            if bouquet == m:
                r = mid
            else:
                l = mid + 1
        return l
