"""3. Compare two dictionaries without using the operator "==" returning True or False.
(Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries,
lists, sets, etc.)"""


equivalent = True


def compare_dictionaries(dict1, dict2):
    global equivalent
    if equivalent is False:
        return equivalent
    for element in dict1:
        if element not in dict2:
            equivalent = False
            return equivalent
        else:
            if dict1[element] is None or isinstance(dict1[element], bool):
                if dict2[element] is not dict1[element]:
                    equivalent = False
                    return equivalent
                continue
            if isinstance(dict1[element], int):
                if not isinstance(dict2[element], int):
                    equivalent = False
                    return equivalent
                else:
                    if dict1[element] ^ dict2[element] != 0:
                        equivalent = False
                        return equivalent
                continue
            for dict_el in dict1[element]:
                if dict_el not in dict2[element]:
                    equivalent = False
                    return equivalent
                if isinstance(dict1[element], dict):
                    if isinstance(dict2[element], dict):
                        compare_dictionaries(dict1[element], dict2[element])
                    else:
                        equivalent = False
                        return equivalent
    return equivalent


def main():
    dict1 = {"a": "ABC", "b": [3, 4], "c": {"unu": 1, "doi": 2}, "e": {22, 33, 44}, "f": True, "g": None,
             "person": {"name": "Ana", "age": 32, "languages": {"python": 3, "C++": 2}}, "d": (11, 12, 13)}
    dict2 = {"a": "ABC", "b": [3, 4], "c": {"unu": 1, "doi": 2}, "e": {22, 33, 44}, "f": True, "g": None,
             "person": {"name": "Ana", "age": 32, "languages": {"python": 3, "C++": 2}}, "d": (11, 12, 13)}
    dict3 = {"a": "ABC", "b": [3, 4], "c": {"unu": 1, "doi": 2}, "e": {22, 33, 44}, "f": True, "g": None,
             "person": {"name": "Ana", "age": 32, "languages": {"py": 3, "C++": 2}}, "d": (11, 12, 13)}
    first_comp = compare_dictionaries(dict1, dict2)
    second_comp = compare_dictionaries(dict2, dict1)
    if first_comp and second_comp:
        print("Dictionaries are equivalent")
    else:
        print("Dictionaries are NOT equivalent")


if __name__ == "__main__":
    main()
