import os
import pytest

from gendiff import generate_diff


DIR_PATH = os.path.dirname(__file__)

test_data = [
    ('json', 'stylish'),
    ('json', 'plain'),
    ('json', 'json'),
    ('yaml', 'stylish'),
    ('yaml', 'plain'),
    ('yaml', 'json'),
    ('yml', 'stylish'),
    ('yml', 'plain'),
    ('yml', 'json'),
]


def get_fixture_path(filename):
    return os.path.join(DIR_PATH, 'fixtures', filename)


def read_file(filename):
    return open(get_fixture_path(filename)).read()


@pytest.mark.parametrize('extension, format_name', test_data)
def test_gendiff(extension, format_name):
    first_file = get_fixture_path('first_file.{0}'.format(extension))
    second_file = get_fixture_path('second_file.{0}'.format(extension))

    actual = generate_diff(first_file, second_file, format_name)
    expected = read_file('result_{0}.txt'.format(format_name)).strip()

    assert actual == expected
