gear_state = 'stop'
quit_state = False


def switch_gear_state(next_gear):
    global quit_state
    global gear_state
    gear_state = next_gear

    # Handle gear states
    # TODO: Probably can use a state machine
    if gear_state == 'start':
        gear_msg = 'Car Started... Ready to go.'
    elif gear_state == 'stop':
        gear_msg = 'Car has stopped.'
    elif gear_state == 'help':
        gear_msg = 'start - Start the car.\nend - Stop the car.\nquit - Exit.\n'
    elif gear_state == 'quit':
        quit_state = True
        gear_msg = 'Exiting.'
    else:
        gear_msg = 'I don\'t understand. Try typing \'help\' if you need instructions.'

    try:
        print(gear_msg, end='\n')
    except:
        print('gear_msg is invalid')


def operate_car():
    while not quit_state:
        gear = input().lower()
        switch_gear_state(gear)


def main():
    print('Operate the car engine. Type help for instructions.', end='\n')
    operate_car()


if __name__ == '__main__':
    main()
