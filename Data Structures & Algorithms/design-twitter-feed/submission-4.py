import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.ts = 0  # global timestamp
        self.tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ts += 1
        self.tweets[userId].append((self.ts, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followees = self.following[userId] | {userId}  # include self
        for followee in followees:
            for tweet in self.tweets[followee]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)  # remove oldest tweet

        return [tweetId for _, tweetId in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
