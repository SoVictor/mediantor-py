from heapq import heappop, heappush
from .i_mediantor import IMediantor


class MediantorHeap(IMediantor):
    def __init__(self):
        self.lower_half: list[int] = list()
        self.upper_half: list[int] = list()

    # O(log N)
    def insert(self, x: int) -> None:
        if not self.lower_half:
            heappush(self.lower_half, -x)
            return

        if x < -self.lower_half[0]:
            heappush(self.lower_half, -x)
        else:
            heappush(self.upper_half, x)

        self.maybe_balance()

    # O(log N)
    def take(self) -> int:
        ans: int = -heappop(self.lower_half)

        self.maybe_balance()

        return ans

    # O(1)
    def size(self) -> int:
        return len(self.lower_half) + len(self.upper_half)

    def maybe_balance(self) -> None:
        if len(self.lower_half) < len(self.upper_half):
            heappush(self.lower_half, -heappop(self.upper_half))
        elif len(self.lower_half) > len(self.upper_half) + 1:
            heappush(self.upper_half, -heappop(self.lower_half))
