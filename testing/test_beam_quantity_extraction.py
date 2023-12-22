import pytest
import pandas as pd

excel_file = "assets/mock_beam_quantity.xlsx"

mock_excel_file = pd.read_excel(excel_file, header=None)


@pytest.mark.parametrize(
    "quantity, expected",
    [
        (3810, 1270),
    ],
)
def test_beam_quantity(quantity: int, expected: int) -> int:
    """This test assesses whether the excel file extracts the correct number of beams.
    The mock_excel_file has a total of 3813 rows, meaning there are 1271 beams (left, middle, right).

    Args:
        quantity (int): The number of beams.
        expected (int): The number of beams.

    Returns:
        int: The number of beams.
    """
    quantity = mock_excel_file[0].iloc[::3]
    assert len(quantity) == expected
