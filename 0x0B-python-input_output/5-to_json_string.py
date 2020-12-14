#!/usr/bin/python3
import json
"SON representation of an object (string):"


def to_json_string(my_obj):
    return json.dumps(my_obj, sort_keys=True)
