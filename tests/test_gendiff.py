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


def test_invalid_extension():
    file1 = "tests/fixtures/file1.txt"
    file2 = "tests/fixtures/file2.txt"
    with pytest.raises(
        ValueError, match='Invalid extension "txt".' " Use json, yaml, yml"
    ):
        generate_diff(file1, file2)


def test_invalid_format():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    with pytest.raises(
        ValueError, match='Invalid format "another". Use stylish, plain, json'
    ):
        generate_diff(file1, file2, "another")
