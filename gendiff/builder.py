def build_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff = {}
    for key in keys:
        if key not in dict1.keys():
            diff[key] = {"type": "added", "value": dict2[key]}
        elif key not in dict2.keys():
            diff[key] = {"type": "deleted", "value": dict1[key]}
        elif dict1[key] == dict2[key]:
            diff[key] = {"type": "unchanged", "value": dict1[key]}
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff[key] = {"type": "nested",
                             "value": build_diff(dict1[key], dict2[key])
                             }
            else:
                diff[key] = {
                    "type": "changed",
                    "old_value": dict1[key],
                    "new_value": dict2[key],
                }
    return diff
