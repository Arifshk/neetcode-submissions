class TimeMap:

    def __init__(self):
        self.history = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history.setdefault(key, []).append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        entries = self.history.get(key, [])
        left, right = 0, len(entries) - 1 
        answer = ""

        while left <= right: 
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                answer = entries[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return answer
