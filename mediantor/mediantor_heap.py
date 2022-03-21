from .i_mediantor import IMediantor
from heapq import heappop, heappush
from typing import Final


class MediantorHeap(IMediantor):
    def __init__(self):
        self._lower_half: list[int] = list()
        self._upper_half: list[int] = list()

    # O(log N)
    def insert(self, x: int) -> None:
        if not self._lower_half:
            heappush(self._lower_half, -x)
            return

        if x < -self._lower_half[0]:
            heappush(self._lower_half, -x)
        else:
            heappush(self._upper_half, x)

        self.maybe_balance()

    # O(log N)
    def take(self) -> int:
        ans: Final[int] = -heappop(self._lower_half)

        self.maybe_balance()

        return ans

    # O(1)
    def size(self) -> int:
        return len(self._lower_half) + len(self._upper_half)

    def maybe_balance(self) -> None:
        if len(self._lower_half) < len(self._upper_half):
            heappush(self._lower_half, -heappop(self._upper_half))
        elif len(self._lower_half) > len(self._upper_half) + 1:
            heappush(self._upper_half, -heappop(self._lower_half))
