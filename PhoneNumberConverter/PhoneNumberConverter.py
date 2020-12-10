NUMBER_MAP = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def convert_digit(digit: str)-> str:
    if(digit not in NUMBER_MAP):
        return "-"
    return NUMBER_MAP[digit]


def convert_phone_number(phone_number: str)-> str:
    number_text = ""
    for digit in phone_number:
        number_text += convert_digit(digit)+' '
    return number_text


def main():
    phone_number = input("Phone Number: ")
    print(convert_phone_number(phone_number))
    return 0


if __name__ == '__main__':
    main()
