import pytest

from algorithms.selection_sort import selectionSort
#@pytest.mark.selection
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
    assert selectionSort(input_list) == expected_output