"""
A Token Bucket is a common rate-limiting mechanism.
It controls how many operations can be performed in a given time by “filling” a bucket with tokens at a fixed rate.
Consumers remove tokens from the bucket to proceed.
If there aren’t enough tokens, the consumer must wait until more tokens are available.

Implement a thread-safe token bucket class with the following properties:
        1.	Initialization Parameters:
        •	max_capacity: Maximum number of tokens in the bucket.
        •	fill_rate: Number of tokens added per second.
        2.	Methods:
        •	fill(): Adds tokens to the bucket according to fill_rate and time elapsed since the last fill.
        •	If the bucket is full, the method should wait until space is available.
        •	get(n): Attempts to acquire n tokens.
        •	If enough tokens are not available, it waits until sufficient tokens are added.
        •	Returns a list of n tokens.
        •	Should raise an error if n <= 0 or n > max_capacity.
        3.	Concurrency Requirements:
        •	Multiple threads may call fill() and get() simultaneously.
        •	Your implementation must ensure thread-safety using locks or conditions.
        4.	Additional Notes:
        •	Tokens can be any integer value (you can randomize them if needed).
        •	Ensure that threads waiting for tokens do not starve.
        •	Optimize for minimal blocking while keeping correctness.
"""

import time
import threading


# This is running within a single process of the server - and each request from a consumer is multiple threads running
class TokenBucket:
    def __init__(self, max_capacity, fill_rate):
        self.tokenQueue = []
        self.max_capacity = max_capacity
        self.fill_rate = fill_rate
        self.last_fill_timestamp = time.time()

        self.not_empty = threading.Condition(threading.Lock())
        self.not_full = threading.Condition(threading.Lock())

    def fill(self):
        with self.not_full:
            if self.max_capacity - len(self.tokenQueue) <= 0:
                self.not_full.wait()

            now = time.time()
            tokens_to_fill = min(
                (now - self.last_fill_timestamp) * self.fill_rate, self.max_capacity
            )
            self.last_fill_timestamp = now

            for _ in range(tokens_to_fill):
                tokens_to_fill.append(random.random(1, 100))

            self.not_empty.notify_all()

    def get(self, n):
        result = []
        tokens_to_get = 0

        while tokens_to_get < n:
            with self.not_empty:
                if n > len(self.tokenQueue):
                    self.not_empty.wait()

                result.append(self.tokenQueue.pop())
                tokens_to_get += 1

                self.not_full.notify_all()

        return result


"""
--------------------------------------------------------------------------------------------------------------------------------------------
"""

import threading
import time
from collections import deque


class TokenBucket:
    def __init__(self, max_capacity, fill_rate):
        self.max_capacity = max_capacity
        self.fill_rate = fill_rate
        self.last_fill_time = time.time()

        self.bucketQueue = deque()

        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def fill(self):
        # this is the same as putting a lock -> Which allows only a single thread to execute the code
        with self.not_full:
            if len(self.bucketQueue) >= self.max_capacity:
                self.not_full.wait()

            now = time.time()

            tokens_to_add = min(
                self.max_capacity - len(self.bucketQueue),
                (now - self.last_fill_time) * self.fill_rate,
            )

            self.last_fill_time = now

            for _ in range(tokens_to_add):
                self.bucketQueue.append(random.random(1, 100))

            self.not_empty.notify_all()  # Now the thread that was invoked to update all buckets is full! We want to have the get threads start accessing since they're not to be starved
            # This in a way invokes the call to get - by telling get threads to be alive

    def get(self, n):
        tokens_to_take = 0
        result = []

        while tokens_to_take < n:
            with self.not_empty:
                if len(self.bucketQueue) == 0:
                    self.not_empty.wait()  # Wait for tokens to come up - this should trigger when notify_all is called in fill

                tokens_to_take -= 1
                result.append(self.bucketQueue.pop())

                self.not_full.notify_all()

        return result


"""
--------------------------------------------------------------------------------------------------------------------------------------------
"""
import threading
import time
import random


class TokenBucket:
    def __init__(self, max_capacity: int, fill_rate: int):
        self.MAX_CAPACITY = max_capacity
        self.FILL_RATE = fill_rate
        self.bucket = []
        self.last_fill_timestamp = time.time()

        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def fill(self):
        with self.not_full:
            while len(self.bucket) >= self.MAX_CAPACITY:
                self.not_full.wait()  # Wait until there is space

            now = time.time()
            # Tokens to add based on elapsed time and fill rate
            num_tokens_to_add = min(
                self.MAX_CAPACITY - len(self.bucket),
                int((now - self.last_fill_timestamp) * self.FILL_RATE),
            )
            self.last_fill_timestamp = now

            for _ in range(num_tokens_to_add):
                self.bucket.append(random.randint(1, 100))

            if num_tokens_to_add > 0:
                print(
                    f"Filled {num_tokens_to_add} tokens, bucket size: {len(self.bucket)}"
                )
            self.not_empty.notify_all()  # Wake up consumers

    def get(self, n: int):
        if n <= 0:
            raise ValueError("Cannot get zero or negative tokens.")
        if n > self.MAX_CAPACITY:
            raise ValueError("Cannot get more tokens than max capacity.")

        result = []
        token_acquired = 0

        while token_acquired < n:
            with self.not_empty:
                while len(self.bucket) < 1:
                    self.not_empty.wait()  # Wait for tokens

                result.append(self.bucket.pop())
                token_acquired += 1
                self.not_full.notify_all()  # Wake up fillers

        print(f"Got tokens: {result}")
        return result


# -------------------------
# Example: Manual threads
# -------------------------
bucket = TokenBucket(max_capacity=10, fill_rate=2)


def filler_task():
    while True:
        bucket.fill()
        time.sleep(1)  # Simulate time between fill attempts


def consumer_task(n):
    while True:
        bucket.get(n)
        time.sleep(random.uniform(0.5, 2))  # Random delay between consuming


# Create manual threads
threads = []
threads.append(threading.Thread(target=filler_task))
threads.append(threading.Thread(target=consumer_task, args=(3,)))
threads.append(threading.Thread(target=consumer_task, args=(2,)))
threads.append(threading.Thread(target=consumer_task, args=(5,)))

# Start all threads
for t in threads:
    t.start()
