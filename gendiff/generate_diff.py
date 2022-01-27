import json


def generate_diff(first_file, second_file):
    first = json.load(open(first_file))
    second = json.load(open(second_file))

    uniq_keys = sorted(first.keys() | second.keys())

    def build(key):
        if not key in second:
            return f' - {key}: {first[key]}'
        if not key in first:
            return f' + {key}: {second[key]}'
        if first[key] == second[key]:
            return f'   {key}: {first[key]}'

        return f' - {key}: {first[key]}\n  + {key}: {second[key]}'

    return '{\n ' + '\n '.join(map(build, uniq_keys)) + '\n}'
