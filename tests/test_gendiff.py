import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, expected, format",
    [
        (
            "tests/fixtures/file1_plain.json",
            "tests/fixtures/file2_plain.json",
            "tests/fixtures/result_plain.txt",
            "stylish",
        ),
        (
            "tests/fixtures/file1_plain.yaml",
            "tests/fixtures/file2_plain.yaml",
            "tests/fixtures/result_plain.txt",
            "stylish",
        ),
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/result.txt",
            "stylish",
        ),
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.yaml",
            "tests/fixtures/result.txt",
            "stylish",
        ),
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/result_plain_format.txt",
            "plain",
        ),
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.yaml",
            "tests/fixtures/result_plain_format.txt",
            "plain",
        ),
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "tests/fixtures/result_json_format.txt",
            "json",
        ),
        (
            "tests/fixtures/file1.yaml",
            "tests/fixtures/file2.yaml",
            "tests/fixtures/result_json_format.txt",
            "json",
        ),
    ],
)
def test_generate_diff(file1, file2, expected, format):
    result = open(expected)
    result_data = result.read()
    assert generate_diff(file1, file2, format) == result_data


@pytest.mark.parametrize(
    "file1, file2, format",
    [
        (
            "tests/fixtures/file1.txt",
            "tests/fixtures/file2.txt",
            "stylish",
        ),
        (
            "tests/fixtures/file1.json",
            "tests/fixtures/file2.json",
            "another",
        ),
    ],
)
def test_invalid_format(file1, file2, format):
    with pytest.raises(ValueError):
        generate_diff(file1, file2, format)
