import os
import sys
# Ensure package modules in parent directory are importable when pytest runs from different CWDs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sorting.quick_sort import quick_sort
import random
import sys as _sys
from collections import Counter

@pytest.mark.parametrize("arr, expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([4, 3, 6, 1], [1, 3, 4, 6]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),          # already sorted
    ([4, 3, 2, 1], [1, 2, 3, 4]),          # reverse
    ([6, 3, 3, 2, 1], [1, 2, 3, 3, 6]),    # mixed
    ([9, 7, 8, 6, 4, 10, 5, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),    # 10 elements
    ([3, 3, 3], [3, 3, 3]),                # all equal
    ([2, 3, 2, 1, 3], [1, 2, 2, 3, 3]),    # duplicates
    ([-1, -3, 2, 0], [-3, -1, 0, 2]),      # negatives + zero
    ([1.5, 1.2, 1.2, -0.3], [-0.3, 1.2, 1.2, 1.5]),  # floats
])
def test_quick_sort_basic(arr, expected):
    data = arr.copy()
    out = quick_sort(data)
    assert out == expected
    assert data == expected   

# in-place modification should also result in the sorted order
def test_quick_sort_returns_same_list_object():
    data = [3, 1, 2]
    out = quick_sort(data)
    assert out is data

# test for preserving elements
def test_quick_sort_preserves_elements():
    data = [5, 1, 5, 2, 5, -1, 2]
    before = Counter(data)
    quick_sort(data)
    after = Counter(data)
    assert before == after

# test for random input 
def test_quick_sort_random_against_builtin_sorted():
    random.seed(42)
    for _ in range(200):
        data = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        expected = sorted(data)
        quick_sort(data)
        assert data == expected

# test for small input
def test_quick_sort_sorted_input_small_does_not_crash():
    data = list(range(200))   # Don't make it too large to avoid excessive recursion.
    quick_sort(data)
    assert data == list(range(200))

# test for raising errors on uncomparable types
def test_quick_sort_raises_on_uncomparable_types():
    data = [1, "a"]
    with pytest.raises(TypeError):
        quick_sort(data)