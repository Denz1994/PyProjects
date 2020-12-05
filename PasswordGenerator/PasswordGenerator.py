import random
import sys


_SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%']


# Generate a list of upper and lower case letters
def generate_letter_choices(starting_letter, ending_letter):
    char_value = ord(starting_letter)
    ending_letter_value = ord(ending_letter)
    letters = []

    # Add all letters A-z excluding some special characters( ascii 91-96). This is case sensitive.
    while char_value <= ending_letter_value:
        if 91 <= char_value <= 96:
            char_value += 1
        else:
            letters.append(chr(char_value))
            char_value += 1
    return letters


def generate_number_choices(starting_num, ending_num):
    nums = []
    for num in range(starting_num, ending_num):
        nums.append(str(num))
    return nums


def generate_char(letters, numbers, special_characters):
    character = random.choice(letters + numbers + special_characters)
    return character


def generate_password(size):
    password = ''
    number_choices = generate_number_choices(0, 10)
    letter_choices = generate_letter_choices('A', 'z')

    # Build the password from the choices above
    for _ in range(0, size):
        password += generate_char(letter_choices, number_choices, _SPECIAL_CHARACTERS)
    return password


def main(argv):

    # If no arg is passed in just use 15 as the password length
    password_length = int(argv[0]) if argv else 15
    password_length_msg = 'Your password length is {} characters'.format(password_length)
    password_msg = 'Password: {}'.format(generate_password(password_length))
    print('\n' + password_length_msg + '\n' + password_msg + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
