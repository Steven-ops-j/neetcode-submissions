class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.news = defaultdict(list) 
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.news[userId], (self.t, tweetId))
        if len(self.news[userId]) > 10:
            heapq.heappop(self.news[userId])
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = [x for x in self.news[userId]]
        for user in self.follows[userId]:
            for news_id in self.news[user]:
                heapq.heappush(arr, news_id)
                if len(arr) > 10:
                    heapq.heappop(arr)

        return [x[1] for x in sorted(arr)[::-1]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId) 
        
