import pytest

@pytest.fixture(params=[1, 2])
def two(request):
    return request.param

@pytest.fixture(params=[1, 2])
def one(request, two):
    return request.param, two

@pytest.mark.parametrize('arg1,arg2', [
    ('val1', pytest.lazy_fixture('one')),
])
def test_func(arg1, arg2):
    assert arg2 in [1, 2]