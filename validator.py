#!/usr/bin/env python3

"""
Script to validate resources
"""
import os
from pathlib import Path
import json
from jsonschema import validate


def get_category_list():
    """
    Walk the current directory and get a list of all subdirectories at that
    level. These are the "categories" of resources.
    """
    dirs = [
        str(path)
        for path in Path('.').rglob('*.json')
    ]
    return dirs



def get_schema():
    with open("resource.schema", "r") as schema:
        return schema.read()


def validator(schema, resources):
    """
    Given the resource.schema validate if a give resource index adheres to the rules
    """
    for resource in resources:
        with open(resource, "r") as res:
            data = json.loads(res.read())
            validate(instance=data, schema=schema)


if __name__ == "__main__":
    resources = get_category_list()
    schema = json.loads(get_schema())
    validator(schema, resources)
