import os
import pytest

from gendiff.generate_diff import generate_diff


DIR_PATH = os.path.dirname(__file__)


def get_fixture_path(filename):
    return os.path.join(DIR_PATH, 'fixtures', filename)


def read_file(filename):
    return open(get_fixture_path(filename)).read()


@pytest.mark.parametrize('extension', ['json', 'yaml'])
def test_gendiff(extension):
    first_file = get_fixture_path('first_file.{0}'.format(extension))
    second_file = get_fixture_path('second_file.{0}'.format(extension))

    actual = generate_diff(first_file, second_file)
    expected = read_file('result.txt').strip()

    assert actual == expected
