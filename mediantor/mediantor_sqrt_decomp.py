from collections import deque
from .i_mediantor import IMediantor
from math import sqrt


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
            if self.buckets[bucket_idx][i] > x:
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
