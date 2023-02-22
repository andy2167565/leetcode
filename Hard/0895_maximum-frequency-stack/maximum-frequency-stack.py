import collections
class FreqStack:

    def __init__(self):
        self.valfreq = collections.Counter()  # Key is val and value is the frequency of that val
        self.freqmap = collections.defaultdict(list)  # Key is frequency and value is a stack of vals with that frequency
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.valfreq[val] += 1  # Add 1 frequency to val
        self.maxfreq = max(self.maxfreq, self.valfreq[val])  # Update maxfreq
        self.freqmap[self.valfreq[val]].append(val)  # Add val to its current frequency

    def pop(self) -> int:
        val = self.freqmap[self.maxfreq].pop()  # Get the latest val with maxfreq
        if not self.freqmap[self.maxfreq]:  # Decrease maxfreq by 1 if there is no vals with maxfreq
            self.maxfreq -= 1
        self.valfreq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
