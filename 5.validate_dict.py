"""5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
dictionary that has strings as keys and values) and a dictionary.
A rule is defined as follows: (key, "prefix", "middle", "suffix").
A value is considered valid if it starts with "prefix", "middle" is inside the value(not at the beginning or end)
and ends with "suffix".The function will return True if the given dictionary matches all the rules, False otherwise.

Example:
the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are
respected for "key1" and "key2" "key3" that does not appear in the rules."""


def validate_dict(rules, my_dict):
    valid_dict = False
    for key, value in my_dict.items():
        for rule in rules:
            if key in rule:
                if value.startswith(rule[1]) and value.endswith(rule[3]):
                    if rule[2] in value[len(rule[1]):-len(rule[3])]:
                        valid_dict = True
    return valid_dict


def main():

    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    my_dict = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    valid_dict = validate_dict(rules, my_dict)

    if valid_dict:
        print("The dictionary is valid")
    else:
        print("The dictionary is not valid")

    rules_1 = {("key1", "str", "inside", "end"), ("key2", "this", "dict", "valid"), ("key3", "o", "a", " ")}
    my_dict_1 = {"key1": "str come inside, it's too cold out end", "key2": "this is dict is valid",
                 "key3": "once upon a time "}

    valid_dict_1 = validate_dict(rules_1, my_dict_1)

    if valid_dict_1:
        print("Valid")
    else:
        print("Not valid")


if __name__ == "__main__":
    main()
