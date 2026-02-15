"""
This question is usually on a phone screen or a new graduate onsite.

Design a hit counter to record the number of hits on a webpage for the last 5 minutes.

Questions:
1. Does this need to be threadsafe?
2. Does the time window need to be resizeable?
"""

import time
from collections import deque
import threading


class HitCounter:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def view(self):
        now = time.time()
        with self.lock:
            while now - self.queue[0] >= 300:
                self.queue.popleft()

            self.queue.append(time.time())
            return len(self.queue)


"""
------------------------------------------------------------------------------------------------------------------------------------
"""

import time
from collections import deque


class HitCounter:
    def __init__(self):
        self.start = 0
        self.hits = []
        self.seconds = 5 * 60
        self.hitsDeque = deque()

    def pageView(self):
        timestamp = time.time()

        self.hits.append(timestamp)

        while timestamp - self.hits[self.start] > self.seconds:
            self.start += 1

        return len(self.hits) - self.start

    def pageViewDeque(self):
        timestamp = time.time()

        self.hitsDeque.append(timestamp)

        while timestamp - self.hitsDeque[0] >= self.seconds:
            self.hitsDeque.popleft()

        return len(self.hitsDeque)


# 1. Does this need to be threadsafe?

# Yes multiple applications could be trying to access the API leading


# High performance optimization don't understand
