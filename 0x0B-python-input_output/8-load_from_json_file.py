#!/usr/bin/python3
"writes an Object to a text file"
import json


def load_from_json_file(filename):
    "writes an Object to a text file"
    with open(filename, "r") as f:
        data = json.load(f)
        return data
