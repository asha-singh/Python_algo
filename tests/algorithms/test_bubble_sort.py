import pytest

from algorithms.bubble_sort import bubbleSort

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
def test_bubbleSort(input_list, expected_output):
    assert bubbleSort(input_list) == expected_output