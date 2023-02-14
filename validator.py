#!/usr/bin/env python3

"""
Script to validate resources
"""

from pathlib import Path
import json
from jsonschema import validate


def get_category_list():
    """
    Walk the current directory and get a list of all subdirectories at that
    level. These are the "categories" of resources.
    """
    dirs = []

    for path in Path('.').rglob('*.json'):
        path = str(path)
        if "venv" not in path:
            dirs.append(path)
            
    return dirs



def get_schema():
    """
    Get resource schema content
    """
    with open("resource.schema", "r",  encoding='UTF-8') as schema_content:
        return schema_content.read()


def validator(schema, resources):
    """
    Given the resource.schema validate if a give resource index adheres to the rules
    """
    total_resources = 0
    for resource in resources:
        with open(resource, "r", encoding='UTF-8') as res:
            data = json.loads(res.read())
            total_resources = total_resources + len(data["resources"])
            validate(instance=data, schema=schema)
    print("All resources adhere to the schema ✅")
    print("Total Resources:", total_resources)


if __name__ == "__main__":
    resources = get_category_list()
    json_schema = json.loads(get_schema())
    validator(json_schema, resources)
