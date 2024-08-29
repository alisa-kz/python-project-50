import json


def to_json(tree):
    """
    Implements "json" formatting.

    Arguments:
    tree (dict): The diff dictionary
    """
    return json.dumps(tree, indent=2)
