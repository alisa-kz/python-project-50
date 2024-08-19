import json
import yaml


def read_file(path):
    if path[-4:] == 'json':
        data = json.load(open(path))
    else:
        data = yaml.safe_load(open(path))
    return data
