from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    result = open("tests/fixtures/result.txt")
    result_data = result.read()
    assert generate_diff(file1, file2) == result_data
