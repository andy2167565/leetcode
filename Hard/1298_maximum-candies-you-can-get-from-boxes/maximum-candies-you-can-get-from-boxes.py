class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
        open = [box for box in boxes if status[box]]
        for curr in open:
            for nxt in containedBoxes[curr]:
                boxes.add(nxt)
                if status[nxt]:
                    open.append(nxt)
            for nxt in keys[curr]:
                if not status[nxt] and nxt in boxes:
                    open.append(nxt)
                status[nxt] = 1
        return sum(candies[box] for box in open)
