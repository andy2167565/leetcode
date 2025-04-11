class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        import collections
        if len(set(suits)) == 1:
            return "Flush"
        match max(collections.Counter(ranks).values()):
            case 5 | 4 | 3:
                return "Three of a Kind"
            case 2:
                return "Pair"
            case _:
                return "High Card"
