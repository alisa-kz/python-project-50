import itertools


def format(tree):
    lines = []
    for key, dict_value in tree.items():
        if dict_value["type"] == "deleted":
            line = (f"  - {key}: {str(dict_value["value"]).lower()}")
        elif dict_value["type"] == "added":
            line = (f"  + {key}: {str(dict_value["value"]).lower()}")
        elif dict_value["type"] == "unchanged":
            line = (f"    {key}: {str(dict_value["value"]).lower()}")
        else:
            line1 = (f"  - {key}: {str(dict_value["old_value"]).lower()}")
            line2 = (f"  + {key}: {str(dict_value["value"]).lower()}")
            line = line1 + "\n" + line2
        lines.append(line)
    result = itertools.chain("{", lines, "}")
    return "\n".join(result)


def stylish(value, replacer=" ", spaces_count=4):

    def iter_(current_value, depth=0):
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        if not isinstance(current_value, dict):
            return str(current_value)
        if 'type' in current_value.keys():
            return iter_(current_value.get('value'), deep_indent_size - spaces_count)
        for key, val in current_value.items():
            lines.append(f"{deep_indent[:-2]}  {key}: {iter_(val, deep_indent_size)}")
        result = itertools.chain("{", lines, [current_indent + "}"])
        return "\n".join(result)
    return iter_(value)
