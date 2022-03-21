from collections import deque
from math import sqrt
from typing import Final

from .i_mediantor import IMediantor


class MediantorSqrtDecomp(IMediantor):
    def __init__(self, max_size: int):
        self._size: int = 0
        self._bucket_size: int = max(1, int(sqrt(max_size)))
        self._buckets: list[deque[int]] = list()

    # O(sqrt(N)).
    def insert(self, x: int) -> None:
        if self._size == 0:
            self._buckets.append(deque())
            self._buckets[0].append(x)
            self._size += 1
            return

        bucket_idx: int = len(self._buckets) - 1
        while bucket_idx > 0 and self._buckets[bucket_idx][0] > x:
            bucket_idx -= 1

        inserted: bool = False
        for i in range(len(self._buckets[bucket_idx])):
            if self._buckets[bucket_idx][i] > x:
                self._buckets[bucket_idx].insert(i, x)
                inserted = True
                break
        if not inserted:
            self._buckets[bucket_idx].append(x)

        for i in range(bucket_idx, len(self._buckets) - 1):
            self._buckets[i + 1].appendleft(self._buckets[i].pop())
        if len(self._buckets[-1]) > self._bucket_size:
            t: Final[int] = self._buckets[-1].pop()
            self._buckets.append(deque())
            self._buckets[-1].append(t)

        self._size += 1

    # O(sqrt(N)).
    def take(self) -> int:
        idx: Final[int] = (self._size - 1) // 2
        bucket_idx: Final[int] = idx // self._bucket_size
        idx_in_bucket: Final[int] = idx % self._bucket_size

        ans: Final[int] = self._buckets[bucket_idx][idx_in_bucket]
        del self._buckets[bucket_idx][idx_in_bucket]

        for i in range(bucket_idx, len(self._buckets) - 1):
            self._buckets[i].append(self._buckets[i + 1].popleft())
        if not self._buckets[-1]:
            self._buckets.pop()

        self._size -= 1

        return ans

    # O(1)
    def size(self) -> int:
        return self._size
