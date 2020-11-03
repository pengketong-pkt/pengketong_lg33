def test_file2_1(try_module):
    print
    "test_file2_1 something"
    assert 2 == 2


def test_file2_2(try_function):
    print
    "test_file2_2 something"
    assert "a" * 3 == "aaa"


def test_file2_3(try_session):
    print
    "test_file2_3 something"
    assert "a" * 3 == "aaa"


def test_file2_4():
    print
    "test_file2_4 something"
    assert "a" * 3 == "aaa"


def test_file2_5(try_function):
    print
    "test_file2_5 something"
    assert "a" * 3 == "aaa"
