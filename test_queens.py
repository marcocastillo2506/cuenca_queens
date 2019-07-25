from nqueens.travis import nqueens
import pytest

def test_nqueens():
    assert nqueens(4) == 2
    assert nqueens(6) == 4
    assert nqueens(8) == 92
