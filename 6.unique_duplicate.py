"""6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
unique elements in the list, and b representing the number of duplicate elements in the list
(use sets to achieve this objective)."""


def unique_and_duplicates(my_list):
    unique = []
    duplicate = []
    one_of_each = set(my_list)
    print(one_of_each, "one of each")
    for element in one_of_each:
        temp = my_list.pop(my_list.index(element))
        if element in my_list:
            duplicate.append(element)
        else:
            unique.append(element)
    return unique, duplicate


def main():

    my_list = [1, "a", 1, "b", 2, 2, "c", 3, 3, 3, "d", 4, 4]
    unique, duplicate = unique_and_duplicates(my_list)

    print("Unique elements are: ", unique)
    print("Duplicates elements are: ", duplicate)


if __name__ == "__main__":
    main()
