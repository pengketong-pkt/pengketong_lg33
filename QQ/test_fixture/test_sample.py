import pytest


# def test_equal(data):
#     print
#     data[0]
#     assert data[0] == 1
class TestAdd(object):

    def test1(self, try_session):
        print
        "test1 something"
        assert 4 == 4

    def test2(self, try_module):
        print
        "test2 something"
        assert 5 == 5

    def test3(self, try_class):
        print
        "test3 something"
        assert 5 == 5

    def test4(self, try_function):
        print
        "test4 something"
        assert 5 == 5

    def test5(self):
        print
        "test5 something"
        assert 5 == 5
