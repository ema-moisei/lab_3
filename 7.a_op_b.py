"""7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b
 are two sets, and op is the applied operator: |, &, -.
Ex: {1,2}, {2, 3} =>
{
    "{1, 2} | {2, 3}":  {1, 2, 3},
    "{1, 2} & {2, 3}":  { 2 },
    "{1, 2} - {2, 3}":  { 1 },
    ...
}        """


def a_op_b(*sets):
    op_dict = {}
    all_sets = list(sets)
    while all_sets:
        first_set = all_sets.pop(0)
        if all_sets:
            for second_set in all_sets:
                intersection = first_set.intersection(second_set)
                int_str = str(first_set) + " & " + str(second_set)
                op_dict[int_str] = intersection

                reunited = first_set.union(second_set)
                re_str = str(first_set) + " | " + str(second_set)
                op_dict[re_str] = reunited

                first_set_second_set = first_set.difference(second_set)
                a_b_str = str(first_set) + " - " + str(second_set)
                op_dict[a_b_str] = first_set_second_set

                second_set_first_set = second_set.difference(first_set)
                b_a_str = str(second_set) + " - " + str(first_set)
                op_dict[b_a_str] = second_set_first_set

    return op_dict


def main():

    op_dict = a_op_b({1, 2}, {2, 3}, {2, 5, 11}, {5, 8, 9})
    for key, value in op_dict.items():
        print(key, ":", value)


if __name__ == "__main__":
    main()
