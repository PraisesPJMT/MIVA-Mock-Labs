import pytest
from module_fixed import crEate_mOdule, str_concatenate, division_operation, list_indexing_example

# Part B1: Black-box testing
@pytest.mark.parametrize("num_list, expected_sum, expected_avg", [
    ([10, 20, 30], 60, 20),
    ([0, 0, 0], 0, 0),
    ([5], 5, 5),  # boundary: single element
    ([], None, None),  # empty list edge case
])

def test_crEate_mOdule_blackbox(num_list, expected_sum, expected_avg):
    total, avg = crEate_mOdule(num_list)
    assert total == expected_sum
    assert avg == expected_avg

@pytest.mark.parametrize("p1, p2, expected", [
    ("MIVA", "Open University", "MIVA Open University"),
    ("", "Test", " Test"),
    ("Hello", "", "Hello "),
])
def test_str_concatenate_blackbox(p1, p2, expected):
    assert str_concatenate(p1, p2) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (0, 1, 0),
])
def test_division_operation_valid(a, b, expected):
    assert division_operation(a, b) == expected

def test_division_operation_zero():
    result = division_operation(10, 0)
    assert result is None

@pytest.mark.parametrize("items, idx, expected", [
    (["MIVA","Open","Uni"], 0, "MIVA"),
    (["MIVA","Open","Uni"], 2, "Uni"),
])

def test_list_indexing_valid(items, idx, expected):
    assert list_indexing_example(items, idx) == expected

def test_list_indexing_out_of_range():
    result = list_indexing_example(["a", "b"], 5)
    assert result is None

# Part B2: White-box testing to cover branches and paths
def test_crEate_mOdule_empty_list():
    total, avg = crEate_mOdule([])
    assert total is None and avg is None

def test_str_concatenate_exception_handling():
    result = str_concatenate("MIVA", None)
    assert result == ""

def test_division_good_and_bad_paths():
    assert division_operation(10, 2) == 5
    assert division_operation(10, 0) is None

def test_list_indexing_all_paths():
    assert list_indexing_example(["a"], 0) == "a"
    assert list_indexing_example(["a"], 1) is None
