from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3, 4], -8, "test") == "test"
    assert arrs.get([1, 2, 3, 4], -2, "test") == 3
    assert arrs.get([4, 6, 8], 5, "test") == "test"



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 5) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -1) == [5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6], 0, -1) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5, 6], -6, -1) == [1, 2, 3, 4, 5]



