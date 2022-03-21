from .i_mediantor import IMediantor
from typing import Final


class MediantorSortedList(IMediantor):
    def __init__(self):
        self._elements: list[int] = list()

    # O(N)
    def insert(self, x: int) -> None:
        for i in range(len(self._elements)):
            if self._elements[i] > x:
                self._elements.insert(i, x)
                return

        self._elements.append(x)

    # O(N)
    def take(self) -> int:
        idx: Final[int] = (len(self._elements) - 1) // 2
        return self._elements.pop(idx)

    # O(1)
    def size(self) -> int:
        return len(self._elements)
