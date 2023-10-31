#!/usr/bin/env python3


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

big_dict = {} # can be a list too
term_searched = "your term" # can be any type of value except list or dict, update the script for your needs.


find_path(big_dict, term_searched)
