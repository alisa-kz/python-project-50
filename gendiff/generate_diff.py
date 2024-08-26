import gendiff.formatters
from gendiff.parser import read_file
from gendiff.builder import build_diff


def generate_diff(file1, file2, format='stylish'):
    data1 = read_file(file1)
    data2 = read_file(file2)
    diff = build_diff(data1, data2)
    make_style = gendiff.formatters.to_format(format)
    return make_style(diff)
