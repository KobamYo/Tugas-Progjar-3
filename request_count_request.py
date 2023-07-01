from itertools import count


class Counter:
    def __init__(self):
        self._request_count = 0
        self._counter = count()

    def increment(self):
        next(self._counter)

    def get_count(self):
        self._request_count += 1
        return self._request_count
