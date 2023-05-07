import collections
class FrequencyTracker:

    def __init__(self):
        self.freq = collections.defaultdict(int)  # {number: frequency}
        self.count = collections.defaultdict(int)  # {frequency: count}

    def add(self, number: int) -> None:
        if number in self.freq:  # Subtract the count of previous frequency by 1
            if self.count[self.freq[number]] > 1:
                self.count[self.freq[number]] -= 1
            else:
                self.count.pop(self.freq[number])
        self.freq[number] += 1
        self.count[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            if self.count[self.freq[number]] > 1:
                self.count[self.freq[number]] -= 1
            else:
                self.count.pop(self.freq[number])
            if self.freq[number] > 1:
                self.freq[number] -= 1
                self.count[self.freq[number]] += 1  # Add the count of current frequency by 1
            else:
                self.freq.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.count


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
