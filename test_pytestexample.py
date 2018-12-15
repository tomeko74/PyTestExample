import pytest
import pytestexample
from pytestexample import StudentDB


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ]
                         )
def test_add(num1, num2, result):
    assert pytestexample.add(num1, num2) == result


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (5, 5, 25),
                             ('Hello ', 3, 'Hello Hello Hello '),
                             (1.5, 1.5, 2.25)
                         ]
                         )
def test_product(num1, num2, result):
    assert pytestexample.product(num1, num2) == result


@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('----------teardown----------------')
    db.close()


def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'


'''
@pytest.mark.number
def test_add():
    assert pytestexample.add(7, 3) == 10
    assert pytestexample.add(7) == 9


@pytest.mark.number
def test_product():
    assert pytestexample.product(5, 5) == 25
    assert pytestexample.product(5) == 10


@pytest.mark.strings
def test_add_strings():
    result = pytestexample.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result


@pytest.mark.string
def test_product_strings():
    assert pytestexample.product('Hello ', 3) == 'Hello Hello Hello '
    result = pytestexample.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
'''



