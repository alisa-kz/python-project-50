from gendiff.parser import read_file
from gendiff.formatters import stylish, plain, json
from gendiff.builder import build_diff


def generate_diff(file1, file2, format='stylish'):
    if format == 'stylish':
        to_format = stylish.to_stylish
    elif format == 'plain':
        to_format = plain.to_plain
    elif format == 'json':
        to_format = json.to_json
    data1 = read_file(file1)
    data2 = read_file(file2)
    diff = build_diff(data1, data2)
    return to_format(diff)
