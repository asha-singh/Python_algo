import pytest

from algorithms.insertion_sort import insertionSort
#@pytest.mark.insertion
@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (
            [4, 3, 5, 2, 1],
            [1, 2, 3, 4, 5]
        ),
        (
            [3, 1, 2],
            [1, 2, 3]
        )
    ]
)
#@pytest.mark.insertion
def testSelectedSort(input_list, expected_output):
    assert insertionSort(input_list) == expected_output