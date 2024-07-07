# Reference: https://leetcode.com/problems/online-election/solutions/173382/c-java-python-binary-search-in-times/
import collections, bisect
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times, self.leads = times, []
        counter, lead = collections.defaultdict(int), -1
        for p in persons:
            counter[p] += 1
            if counter[p] >= counter[lead]:  # Update the current vote leader
                lead = p
            self.leads.append(lead)

    def q(self, t: int) -> int:
        return self.leads[bisect.bisect(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
