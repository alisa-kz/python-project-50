import json
import itertools


def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)
    diff = build_diff(data1, data2)
    return format(diff)


def read_file(path):
    data = json.load(open(path))
    return data


def build_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff = {}
    for key in keys:
        if key not in dict1.keys():
            diff[key] = {'type': 'added', 'value': dict2[key]}
        elif key not in dict2.keys():
            diff[key] = {"type": "deleted", "value": dict1[key]}
        elif dict1[key] == dict2[key]:
            diff[key] = {"type": "unchanged", "value": dict1[key]}
        else:
            diff[key] = {
                "type": "changed",
                "old_value": dict1[key],
                "new_value": dict2[key]
            }
    return diff


def format(tree):
    lines = []
    for key, dict_value in tree.items():
        if dict_value["type"] == "deleted":
            line = '  - ' + key + ': ' + str(dict_value["value"]).lower()
        elif dict_value["type"] == "added":
            line = "  + " + key + ": " + str(dict_value["value"]).lower()
        elif dict_value["type"] == "unchanged":
            line = "    " + key + ": " + str(dict_value["value"]).lower()
        else:
            line1 = "  - " + key + ": " + str(dict_value["old_value"]).lower()
            line2 = "  + " + key + ": " + str(dict_value["new_value"]).lower()
            line = line1 + '\n' + line2
        lines.append(line)
    result = itertools.chain("{", lines, "}")
    return "\n".join(result)
