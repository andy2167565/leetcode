class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
#======== <Solution 1> ========#
        for row in board + list(zip(*board)):
            for s in ''.join(row).split('#'):
                for w in word, word[::-1]:
                    if len(s) == len(w) and all(ss in (' ', ww) for ss, ww in zip(s, w)):
                        return True
        return False

#======== <Solution 2> ========#
        import itertools
        for row in board + list(zip(*board)):
            for k, g in itertools.groupby(row, key=lambda x: x != '#'):
                g = list(g)
                if k and len(g) == len(word):
                    for w in word, word[::-1]:
                        if all(gg in (' ', ww) for gg, ww in zip(g, w)):
                            return True
        return False
