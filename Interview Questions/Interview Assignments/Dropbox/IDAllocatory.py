# Q: Design a system that is ID Allocator
# ID Allocator
# Manages -> Assignment and Release of Unique IDs from a pool -> Each Id is only used once
# Have ranges of pool of ID


class IDAllocator:
    def __init__(self):
        self.pool = [i for i in range(1, 1001)]  # Make this minHeap
        self.used = {}

    def allocateID(self, components: list[str]) -> bool:
        if len(components) > len(self.pool):
            return False

        for c in components:
            id = self.pool.pop(0)  # O(n)

            self.used[c] = id

        return True

    def _firstOccurence(self, idToRelease):
        left, right = 0, len(self.pool) - 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if self.pool[mid] >= idToRelease:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        self.pool = self.pool[:ans] + [idToRelease] + self.pool[ans:]  # O(n)

    def releaseID(self, component: str) -> bool:
        if component not in self.used:
            return False

        idToRelease = self.used[component]

        self.used.pop(component)

        self._firstOccurence(idToRelease)

        return True
