from gendiff.parser import read_file
from gendiff.formatter import stylish
from gendiff.builder import build_diff


def generate_diff(file1, file2, format=stylish):
    data1 = read_file(file1)
    data2 = read_file(file2)
    diff = build_diff(data1, data2)
    return format(diff)
