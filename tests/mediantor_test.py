import os

import pytest

from mediantor import IMediantor, Mediantor, make_mediantor

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


@pytest.mark.parametrize('mediantor_type', MEDIANTORS_LIST)
def test_on_data(mediantor_type: Mediantor):
    for input_filename in os.listdir("tests/data"):
        if not input_filename.endswith(".in"):
            continue

        input_path: str = "tests/data/" + input_filename
        ans_path: str = input_path[:-2] + "out"
        with open(input_path, "r") as input_file, open(ans_path, "r") as ans_file:
            n = int(input_file.readline())

            mediantor: IMediantor = make_mediantor(mediantor_type, n)

            for _ in range(n):
                numbers: list[int] = list(map(int, input_file.readline().split()))
                operation: int = numbers[0]
                if operation == 1:
                    x: int = numbers[1]
                    mediantor.insert(x)
                else:
                    x: int = int(ans_file.readline())
                    assert x == mediantor.take()
