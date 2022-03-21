from enum import Enum

from .i_mediantor import IMediantor
from .mediantor_heap import MediantorHeap
from .mediantor_sorted_list import MediantorSortedList
from .mediantor_sqrt_decomp import MediantorSqrtDecomp


class Mediantor(Enum):
    HEAP = 0
    SQRT_DECOMP = 1
    SORTED_LIST = 2


def make_mediantor(mediantor_type: Mediantor, max_size: int) -> IMediantor:
    if mediantor_type == Mediantor.HEAP:
        return MediantorHeap()
    elif mediantor_type == Mediantor.SQRT_DECOMP:
        return MediantorSqrtDecomp(max_size)
    elif mediantor_type == Mediantor.SORTED_LIST:
        return MediantorSortedList()
