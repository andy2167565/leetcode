class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        import collections
        curr = seen = {id}
        for _ in range(level):
            curr = {friend for person in curr for friend in friends[person] if friend not in seen}
            seen |= curr
        counter = collections.Counter(video for person in curr for video in watchedVideos[person])
        return sorted(sorted(counter), key=counter.get)
