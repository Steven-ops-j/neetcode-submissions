class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = [(timestamp, value)]
        else:
            self.tm[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        arr = self.tm.get(key)
        if not arr:
            return ""
        l, r = 0, len(arr) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            ts = arr[mid][0]
            if ts > timestamp:
                r = mid - 1
            elif ts < timestamp:
                l = mid + 1
                ans = arr[mid][-1]
            else:
                return arr[mid][-1]
        return ans
