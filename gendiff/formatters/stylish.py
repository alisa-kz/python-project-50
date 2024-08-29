import itertools


def to_str(value, depth, replacer=' ', space_count=4):
    """
    Converts value to string.

    Arguments:
    value (bool, int, list, dict): Value to convert
    depth (int): Depth
    replacer (str): Symbol to replace (default ' ')
    space_count (int): Replacers count (default 4)
    """
    indent = replacer * space_count
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'{indent * depth + indent[:-2]}  '
                         f'{key}: {to_str(val, depth + 1)}')
        result = itertools.chain("{", lines, [indent * depth + "}"])
        return "\n".join(result)
    return str(value)


def to_stylish(tree, replacer=' ', space_count=4):
    """
    Implements "stylish" formatting.

    Arguments:
    tree (dict): The diff dictionary
    replacer (str): Symbol to replace (default ' ')
    space_count (int): Replacers count (default 4)
    """
    def iter_(tree, depth=0):
        indent = replacer * space_count
        lines = []
        for key, value in tree.items():
            match value["type"]:
                case "nested":
                    line = (f"{indent * depth + indent[:-2]}  {key}: "
                            f"{iter_(value.get("value"), depth + 1)}")
                case "deleted":
                    line = (f"{indent * depth + indent[:-2]}- {key}: "
                            f"{to_str(value.get("value"), depth + 1)}")
                case "added":
                    line = (f"{indent * depth + indent[:-2]}+ {key}: "
                            f"{to_str(value.get("value"), depth + 1)}")
                case "unchanged":
                    line = (f"{indent * depth + indent[:-2]}  {key}: "
                            f"{to_str(value.get("value"), depth + 1)}")
                case "changed":
                    line1 = (f"{indent * depth + indent[:-2]}- {key}: "
                             f"{to_str(value.get("old_value"), depth + 1)}")
                    line2 = (f"{indent * depth + indent[:-2]}+ {key}: "
                             f"{to_str(value.get("new_value"), depth + 1)}")
                    line = line1 + "\n" + line2
            lines.append(line)
        result = itertools.chain("{", lines, [indent * depth + "}"])
        return "\n".join(result)
    return iter_(tree)
