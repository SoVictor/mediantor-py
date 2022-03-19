from abc import ABC, abstractmethod
from collections import deque
from math import sqrt
import heapq


class IMediantor(ABC):
    @abstractmethod
    def insert(self, x: int) -> None:
        pass

    @abstractmethod
    def take(self) -> int:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


class MediantorSortedList(IMediantor):
    def __init__(self):
        self.elements: list[int] = list()

    # O(N)
    def insert(self, x: int) -> None:
        for i in range(len(self.elements)):
            if self.elements[i] > x:
                self.elements.insert(i, x)
                return

        self.elements.append(x)

    # O(N)
    def take(self) -> int:
        idx: int = (len(self.elements) - 1) // 2
        return self.elements.pop(idx)

    # O(1)
    def size(self) -> int:
        return len(self.elements)


class MediantorSqrtDecomp(IMediantor):
    def __init__(self, max_size: int):
        self.size: int = 0
        self.bucket_size: int = max(1, int(sqrt(max_size)))
        self.buckets: list[deque[int]] = list()

    # O(sqrt(N)).
    def insert(self, x: int) -> None:
        if self.size == 0:
            self.buckets.append(deque())
            self.buckets[0].append(x)
            self.size += 1
            return

        bucket_idx: int = len(self.buckets) - 1
        while bucket_idx > 0 and self.buckets[bucket_idx][0] > x:
            bucket_idx -= 1

        inserted: bool = False
        for i in range(len(self.buckets[bucket_idx])):
            if (self.buckets[bucket_idx][i] > x):
                self.buckets[bucket_idx].insert(i, x)
                inserted = True
                break
        if not inserted:
            self.buckets[bucket_idx].append(x)

        for i in range(bucket_idx, len(self.buckets) - 1):
            self.buckets[i + 1].appendleft(self.buckets[i].pop())
        if len(self.buckets[-1]) > self.bucket_size:
            x: int = self.buckets[-1].pop()
            self.buckets.append(deque())
            self.buckets[-1].append(x)

        self.size += 1

    # O(sqrt(N)).
    def take(self) -> int:
        idx: int = (self.size - 1) // 2
        bucket_idx: int = idx // self.bucket_size
        idx_in_bucket = idx % self.bucket_size

        ans: int = self.buckets[bucket_idx][idx_in_bucket]
        del self.buckets[bucket_idx][idx_in_bucket]

        for i in range(bucket_idx, len(self.buckets) - 1):
            self.buckets[i].append(self.buckets[i + 1].popleft())
        if not self.buckets[-1]:
            self.buckets.pop()

        self.size -= 1

        return ans

    # O(1)
    def size(self) -> int:
        return self.size


class MediantorHeap(IMediantor):
    def __init__(self):
        self.lower_half: list[int] = list()
        self.upper_half: list[int] = list()

    # O(log N)
    def insert(self, x: int) -> None:
        if not self.lower_half:
            heapq.heappush(self.lower_half, -x)
            return

        if x < -self.lower_half[0]:
            heapq.heappush(self.lower_half, -x)
        else:
            heapq.heappush(self.upper_half, x)

        self.maybe_balance()

    # O(log N)
    def take(self) -> int:
        ans: int = -heapq.heappop(self.lower_half)

        self.maybe_balance()

        return ans

    # O(1)
    def size(self) -> int:
        return len(self.lower_half) + len(self.upper_half)

    def maybe_balance(self) -> None:
        if len(self.lower_half) < len(self.upper_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.upper_half))
        elif len(self.lower_half) > len(self.upper_half) + 1:
            heapq.heappush(self.upper_half, -heapq.heappop(self.lower_half))
