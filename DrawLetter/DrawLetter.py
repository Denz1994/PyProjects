"""
We will draw a letter using only X characters in the terminal.
For example:

XXXXX
XX
XXXXX
XX
XX
"""

# TODO: Can be continue mapping char and match input file characters to ALPHABET[char]
ALPHABET = {
    'F': [5, 2, 5, 2, 2]
}


def print_with_string_multiplication(char_pattern):
    for x in char_pattern:
        print('X' * x, end='\n')


def print_with_nested_loop(char_pattern):
    for num in char_pattern:
        print_val = ''
        for _ in range(num):
            print_val += 'X'
        print(print_val)


def main():
    pattern = ALPHABET['F']
    print_with_nested_loop(pattern)


if __name__ == '__main__':
    main()
