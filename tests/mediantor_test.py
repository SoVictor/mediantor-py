from mediantor.i_mediantor import IMediantor
from mediantor.mediantor_heap import MediantorHeap


def test_trivial():
    mediantor: IMediantor = MediantorHeap()

    mediantor.insert(1)
    mediantor.insert(2)
    mediantor.insert(3)
    # values: 1, 2, 3

    assert mediantor.take() == 2

    mediantor.insert(2)
    mediantor.insert(4)
    # values: 1, 2, 3, 4

    assert mediantor.take() == 2
