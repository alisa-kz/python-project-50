#!/usr/bin/env python3
from gendiff import generate_diff, cli


def main():
    """
    Outputs the result on the screen.
    """
    file1, file2, format = cli.parse_arguments()
    print(generate_diff(file1, file2, format))


if __name__ == "__main__":
    main()
