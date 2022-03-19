from mediantor import IMediantor, Mediantor, make_mediantor
import pytest


MEDIANTORS_LIST: list[Mediantor] = [Mediantor.HEAP, Mediantor.SQRT_DECOMP, Mediantor.SORTED_LIST]


@pytest.mark.parametrize('mediantor_type', MEDIANTORS_LIST)
def test_trivial(mediantor_type: Mediantor):
    mediantor: IMediantor = make_mediantor(mediantor_type, 4)

    mediantor.insert(1)
    mediantor.insert(2)
    mediantor.insert(3)
    # values: 1, 2, 3

    assert mediantor.take() == 2

    mediantor.insert(2)
    mediantor.insert(4)
    # values: 1, 2, 3, 4

    assert mediantor.take() == 2
