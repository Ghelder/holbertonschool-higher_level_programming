#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    name = list(a_dictionary.keys())[0]
    value = a_dictionary[name]
    for k, v in a_dictionary.items():
        if v > value:
            value = v
            name = k
    return name
