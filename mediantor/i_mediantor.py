from abc import ABC, abstractmethod


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
