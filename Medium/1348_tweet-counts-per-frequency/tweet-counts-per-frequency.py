# Reference: https://leetcode.com/problems/tweet-counts-per-frequency/solutions/503515/python3-linear-scan/
class TweetCounts:

    def __init__(self):
        self.tweets = dict()

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.setdefault(tweetName, []).append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        seconds = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        ans = [0] * ((endTime - startTime) // seconds + 1)
        for recordTime in self.tweets[tweetName]:
            if startTime <= recordTime <= endTime:
                ans[(recordTime - startTime) // seconds] += 1
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
