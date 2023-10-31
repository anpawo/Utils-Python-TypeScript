#!/usr/bin/env python3

# This function is able to find a certain piece of data in a big list/dict.
# For example, if you have a big json file and want to know how to access a certain value,
# if you know the value, you just need to pass the json object to the function and
# the value you're searching for. You can update the condition for the value,
# in case you're searching for a certain type of data or just anything.


def find_path(obj, term):
    path = ""
    if isinstance(obj, dict):
        for key in obj:
            path = find_path(obj[key], term)
            if path != None:
                return f'["{key}"]{path}'
        return None
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            path = find_path(value, term)
            if path != None:
                return f"[{index}]{path}"
        return None
    if obj == term:
        return ""
    else:
        return None

big_dict = {
    "name": {
        "peter": "johns",
        "other": [
            "alix",
            "george"
        ]
    }
}

example_1 = "alix"    # output: ["name"]["other"][0]
example_2 = "johns"   # output: ["name"]["peter"]
example_1 = "george"  # output: ["name"]["other"][1]
