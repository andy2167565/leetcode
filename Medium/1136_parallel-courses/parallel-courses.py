class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        import collections
        blocks = collections.defaultdict(set)
        blockedby = collections.defaultdict(set)
        for pre, nxt in relations:
            blocks[pre].add(nxt)
            blockedby[nxt].add(pre)
        ans = 1
        while blocks or blockedby:
            available = [course for course in blocks if course not in blockedby]
            if not available:
                return -1
            for course in available:
                for blocked in blocks[course]:
                    blockedby[blocked].remove(course)
                    if len(blockedby[blocked]) == 0:
                        del blockedby[blocked]
                del blocks[course]
            ans += 1
        return ans
