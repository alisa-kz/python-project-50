from gendiff.generate_diff import generate_diff


def test_generate_diff_plain():
    file1 = "tests/fixtures/file1_plain.json"
    file2 = "tests/fixtures/file2_plain.json"
    result = open("tests/fixtures/result_plain.txt")
    result_data = result.read()
    assert generate_diff(file1, file2) == result_data


def test_generate_diff_yml_plain():
    file1 = "tests/fixtures/file1_plain.yaml"
    file2 = "tests/fixtures/file2_plain.yaml"
    result = open("tests/fixtures/result_plain.txt")
    result_data = result.read()
    assert generate_diff(file1, file2) == result_data


def test_generate_diff():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    result = open("tests/fixtures/result.txt")
    result_data = result.read()
    assert generate_diff(file1, file2) == result_data


def test_generate_diff_yml():
    file1 = "tests/fixtures/file1.yaml"
    file2 = "tests/fixtures/file2.yaml"
    result = open("tests/fixtures/result.txt")
    result_data = result.read()
    assert generate_diff(file1, file2) == result_data


def test_generate_diff_plain_format():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    result = open("tests/fixtures/result_plain_format.txt")
    result_data = result.read()
    assert generate_diff(file1, file2, "plain") == result_data


def test_generate_diff_plain_format_yml():
    file1 = "tests/fixtures/file1.yaml"
    file2 = "tests/fixtures/file2.yaml"
    result = open("tests/fixtures/result_plain_format.txt")
    result_data = result.read()
    assert generate_diff(file1, file2, "plain") == result_data


def test_generate_diff_json_format():
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    result = open("tests/fixtures/result_json_format.txt")
    result_data = result.read()
    assert generate_diff(file1, file2, "json") == result_data


def test_generate_diff_json_format_yml():
    file1 = "tests/fixtures/file1.yaml"
    file2 = "tests/fixtures/file2.yaml"
    result = open("tests/fixtures/result_json_format.txt")
    result_data = result.read()
    assert generate_diff(file1, file2, "json") == result_data
