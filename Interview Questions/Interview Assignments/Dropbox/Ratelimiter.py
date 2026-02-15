# Q: Design a rate limiter
# Define for period of time the total number of requests an IP address could make
# Need to reset after a period of time from the first request
# Date time library to associate the number of requests

import time


class RateLimiter:
    def __init__(self, numberOfRequests: int, timePeriod: int):
        """
        Initialize rate limiter

        :param numberOfRequests number of requests per IP
        :type numberOfRequests: int
        :param timePeriod: number of requests in a given time period (seconds)
        :type timePeriod: int
        """
        self.numberOfRequests = numberOfRequests
        self.timePeriod = timePeriod
        self.ipFrequencyAndStart = {}

    def incrementRequest(self, ipAddress: str):
        if ipAddress not in self.ipFrequencyAndStart:
            self.ipFrequencyAndStart[ipAddress] = (1, int(time.time()))
            return

        currentTime = int(time.time())

        reqCount, startTime = self.ipFrequencyAndStart[ipAddress]

        if currentTime - startTime < self.timePeriod:
            if reqCount < self.numberOfRequests:
                self.ipFrequencyAndStart[ipAddress] = (reqCount + 1, startTime)
            else:
                raise (f"Invalid Requests have ${currentTime - startTime} remaining")
        else:
            self.ipFrequencyAndStart[ipAddress] = (1, int(time.time()))


# Above does not work if requests in the first time period is under the limit and then the next half of the
# requests is not taking into account the previous halfs slice of requests to complete the request from the previous set
# Use deque or sliding window
# Above is a burst window - so within the edges of the rate limiter boundary it can send *2 of the request
