#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num += 1

    return (num)


a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
