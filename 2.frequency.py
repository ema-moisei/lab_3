"""2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
characters in the character string and the values are the number of occurrences of that character in the given text.
Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
{'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
"""


def get_frequency(string):
    frequency = {}
    for character in string:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency.setdefault(character, 1)
    return frequency


def main():

    string = "Ana has apples."
    frequency = get_frequency(string)
    print(frequency)


if __name__ == "__main__":
    main()
