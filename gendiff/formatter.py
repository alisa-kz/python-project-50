import itertools


def to_str(value, depth, indent='    '):
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


def stylish(tree, indent='    '):
    def iter_(tree, depth=0):
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
