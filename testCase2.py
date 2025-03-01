# test-case-2.py
import pytest
from mysqrt import mysqrt  

def test_mysqrt():
    # Test case for normal positive input
    assert mysqrt(4) == 2

    # Test case for 0
    #assert mysqrt(0) == 0

    # Test case for a larger number
    assert mysqrt(16) == 4

    # Test case for a float number
    assert mysqrt(2.25) == 1.5

    # Test case for negative input (should raise ValueError)
    #with pytest.raises(ValueError):
     #   mysqrt(-1)
