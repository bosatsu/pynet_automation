

import argparse
import yaml
import json
from pprint import pprint

parser = argparse.ArgumentParser(description = 'Convert json to yaml or yaml to json')
parser.add_argument("file")
args = parser.parse_args()
file_name = args.file


def converter(file_name):
    (unused, suffix) = file_name.split('.')
    if suffix in ('json', 'yml', 'yaml'):
        pass
    else:
        sys.exit('''\n\nInvalid filename extention, 
            system looking for '.json', '.yml', or '.yaml' extention''' )

    with open(file_name) as f:
        if suffix in ('json'):
            try:
                new_list = json.load(f)
                new_file = yaml.safe_dump(new_list, default_flow_style=False)
            except ValueError:
                sys.exit("\n\nInvalid file format, was expecting JSON")

        elif suffix in ('yml', 'yaml'):
            try:
                new_list = yaml.load(f)
                new_file = json.dumps(new_list)
            except ValueError:
                sys.exit("\n\nInvalid file format, was expecting YAML")
    return new_file

print converter(file_name)

