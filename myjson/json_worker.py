import json
import os


def dict_to_json(pydict):
    try:
        data_file = open('../data.json', 'w')
        json.dump(pydict, data_file)
    except AttributeError as e:
        print(e)

    print('Ama in game!')


def json_file_to_dict():
    pass