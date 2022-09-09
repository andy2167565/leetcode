class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
#======== <Solution 1> ========#
        if turnedOn > 8: return []
        from itertools import combinations
        H = [1, 2, 4, 8]
        M = [1, 2, 4, 8, 16, 32]
        M_count = min(5, turnedOn)
        H_count = turnedOn - M_count
        ans = []
        while M_count >= 0 and H_count < 4:
            for h in combinations(H, H_count):
                for m in combinations(M, M_count):
                    if sum(h) < 12 and sum(m) < 60:
                        ans.append(f'{sum(h)}:{sum(m):02d}')
            M_count -= 1
            H_count += 1
        return ans

#======== <Solution 2> ========#
        from itertools import combinations
        watch = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        times = []
        for leds in combinations(range(len(watch)), turnedOn):
            h = sum(watch[i] for i in leds if i < 4)
            m = sum(watch[i] for i in leds if i >= 4)
            if h < 12 and m < 60:
                times.append(f'{h}:{m:02d}')
        return times

#======== <Solution 3> ========#
        from itertools import combinations
        M, times = [1, 2, 4, 8, 16, 32, 60, 120, 240, 480], []
        for leds in combinations(M, turnedOn):
            if not {4, 8, 16, 32}.issubset(set(leds)) and not {240, 480}.issubset(set(leds)):
                h, m = divmod(sum(leds), 60)
                times.append(f'{h}:{m:02d}')
        return times

#======== <Solution 4> ========#
        times = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    times.append(f'{h}:{m:02d}')
        return times

#======== <Solution 5> ========#
        return [f'{h}:{m:02d}' for h in range(12) for m in range(60) if f'{h:b}{m:b}'.count('1') == turnedOn]
