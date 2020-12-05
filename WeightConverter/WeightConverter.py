def convert_weight(unit, weight):
    if unit == 'lbs':
        return weight
    else:
        weight = float(weight) * 0.453592
        return '%.2f' % weight


def main():
    weight = int(input('Weight: '))
    unit_choice = input('(L)bs or (K)g: ').lower()
    unit = 'lbs' if unit_choice == 'l' else 'kgs'
    converted_weight = convert_weight(unit, weight)

    print(f'You weigh {converted_weight} {unit}.')


if __name__ == '__main__':
    main()
