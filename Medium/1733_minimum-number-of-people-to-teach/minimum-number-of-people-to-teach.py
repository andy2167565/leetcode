class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        import collections
        languages, no_common = [set(lang) for lang in languages], set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if languages[u].isdisjoint(languages[v]):  # The two users don't have any common languages
                no_common.update([u, v])
        counter = collections.Counter()
        for user in no_common:
            counter.update(languages[user])
        return len(no_common) - max(counter.values(), default=0)  # Teach the most popular language to the minority who don't speak it
