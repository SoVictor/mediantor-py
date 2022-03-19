from abc import ABC, abstractmethod
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
