import sys
sys.path.append('nqueens')
import pytest
from queens import nqueens

def test_nqueens():
    assert nqueens(4) == 2
    assert nqueens(6) == 4
    assert nqueens(8) == 92
