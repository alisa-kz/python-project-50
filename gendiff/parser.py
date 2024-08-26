import os
import json
import yaml


def get_extension(path):
    _, extension_file = os.path.splitext(path)
    return extension_file[1:]


def read_file(path):
    extension = get_extension(path)
    if extension == 'json':
        data = json.load(open(path))
    elif extension == "yaml" or extension == "yml":
        data = yaml.safe_load(open(path))
    else:
        raise ValueError(f'Invalid extension "{extension}".'
                         f' Use json, yaml, yml')
    return data
