class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
#======== <Solution 1> ========#
        stack = []
        for card in sorted(deck)[::-1]:
            stack = [card] + stack[-1:] + stack[:-1]
        return stack

#======== <Solution 2> ========#
        import collections
        q = collections.deque()
        for card in sorted(deck, reverse=True):
            q.rotate()  # Move the card at the bottom to the top
            q.appendleft(card)
        return list(q)
