import pytest

# @pytest.fixture
# def data():
#     return [1, 2, 3]
pytest.fixture(scope="module")


def try_module():
    print
    "#######################module begin####################"
    yield [6, 7, 8]
    print
    "#######################module end####################"


@pytest.fixture()  # 不加(scope="function")默认scope就是function
def try_function():
    print
    "#######################function begin####################"
    yield "just a test about function scope"
    print
    "#######################function end####################"


@pytest.fixture(scope="class")
def try_class(request):
    print
    "#######################class begin####################"

    def end():
        print
        "#######################class end####################"

    request.addfinalizer(end)
    return "just a test about class scope"


@pytest.fixture(scope="package")  # session == package
def try_session(request):
    print
    "#######################session begin####################"

    def end():
        print
        "#######################session end####################"

    request.addfinalizer(end)
    return "just a test about session scope"
