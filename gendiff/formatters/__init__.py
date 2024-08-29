from gendiff.formatters import stylish, plain, json


def to_format(format):
    """
    Defines the format.

    Arguments:
    format (str): Type of formatting
    """
    if format == "stylish":
        return stylish.to_stylish
    elif format == "plain":
        return plain.to_plain
    elif format == "json":
        return json.to_json
    else:
        raise ValueError(f'Invalid format "{format}". Use stylish, plain, json')
