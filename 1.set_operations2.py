"""1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
(a intersected with b, a reunited with b, a - b, b - a)"""


def set_operations(list1, list2):
    intersection = list(set(list1).intersection(list2))
    reunited = list(set(list1).union(set(list2)))
    list1_list2 = list(set(list1).difference(list2))
    list2_list1 = list(set(list2).difference(list1))

    return intersection, reunited, list1_list2, list2_list1


def main():

    list1 = [10, 15, 20, 25, 30, 35, 40]
    list2 = [25, 35, 40, 50, 88]
    intersection, reunited, list1_list2, list2_list1 = set_operations(list1, list2)
    print("a intersected with b is:", intersection)
    print("a reunited with b is: ", reunited)
    print("a - b is: ", list1_list2)
    print("b - a is: ", list2_list1)


if __name__ == "__main__":
    main()
