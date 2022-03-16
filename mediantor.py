from abc import ABC, abstractmethod


class IMediantor(ABC):
    @abstractmethod
    def insert(self, x: int):
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
    def insert(self, x: int):
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
