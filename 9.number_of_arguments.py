"""9. Write a function that receives a variable number of positional arguments and a variable number of keyword
arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.

Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3"""


def nr_of_arg(*args, **kwargs):
    number = 0
    args_list = args
    kwargs_dict = kwargs
    for element in args_list:
        if element in kwargs_dict.values():
            number += 1

    return number


def main():

    number = nr_of_arg(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    print(number)


if __name__ == "__main__":
    main()
