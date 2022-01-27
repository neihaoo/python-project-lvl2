import os
from gendiff.generate_diff import generate_diff


dir_path = os.path.dirname(__file__)


def get_fixture_path(filename):
    return os.path.join(dir_path, 'fixtures', filename)


def read_file(filename):
    return open(get_fixture_path(filename)).read()


def test_gendiff():
    first_file = get_fixture_path('first_file.json')
    second_file = get_fixture_path('second_file.json')

    actual = generate_diff(first_file, second_file)
    expected = read_file('result.txt').strip()

    assert actual == expected
