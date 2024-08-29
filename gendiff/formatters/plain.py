def to_str(value):
    """
    Converts value to string.

    Arguments:
    value (bool, int, list, dict): Value to convert
    """
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if value == '':
        return "''"
    if isinstance(value, int):
        return value
    return f"'{str(value)}'"


def to_plain(tree):
    """
    Implements "plain" formatting.

    Arguments:
    tree (dict): The diff dictionary
    """
    def iter_(tree, ancerity=''):
        lines = []
        for key, value in tree.items():
            if ancerity:
                path = f"{ancerity}.{key}"
            else:
                path = key
            match value["type"]:
                case "nested":
                    line = iter_(value.get("value"), path)
                case "deleted":
                    line = (f"Property '{path}'"
                            f" was removed")
                case "added":
                    line = (f"Property '{path}'"
                            f" was added with value: "
                            f"{to_str(value.get("value"))}")
                case "changed":
                    line = (f"Property '{path}' was updated. From "
                            f"{to_str(value.get("old_value"))} to "
                            f"{to_str(value.get("new_value"))}")
                case "unchanged":
                    continue
            lines.append(line)
        return "\n".join(lines)
    return iter_(tree)
