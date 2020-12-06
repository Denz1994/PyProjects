import numpy

_TARGET = numpy.random.randint(1, 10)


def main():
    chances = 0
    while chances < 3:
        user_choice = eval(input('Choose a number: '))
        if user_choice == _TARGET:
            print('\nCongrats! You chose the correct number: %d' % user_choice)
            return 0
        else:
            print('Try again :(', end='\n')
        chances += 1
    if chances == 3:
        print('Restart the game.', end='\n')


if __name__ == '__main__':
    # TODO: Hard coded to be 1-10 and 3 tries
    print('Launching Guessing Game...\nGuess a number from 1 to 10 in only 3 tries')
    main()
