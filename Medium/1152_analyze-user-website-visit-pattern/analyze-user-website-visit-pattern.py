class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Reference: https://leetcode.com/problems/analyze-user-website-visit-pattern/solutions/899805/detailed-easy-to-follow-python-solution-clearly-explained/
        import collections, itertools
        users = collections.defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):  # Sort by user then time
            users[user].append(site)
        patterns = collections.Counter()
        for user, sites in users.items():
            patterns.update(collections.Counter(set(itertools.combinations(sites, 3))))
        return max(sorted(patterns), key=patterns.get)
