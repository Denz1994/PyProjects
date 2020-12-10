import random


class MyArray:
    my_list = []
    for num in range(10):
        my_list.append(random.randint(0, 50))

    def __init__(self, array=tuple(my_list), verbose=False):
        self.array = array
        self.verbose = verbose

    def validate_find_max(self):
        if self.verbose:
            my_array = MyArray(['3', '4'])

            # Execute two max() implementations
            my_sum = my_array.find_max()
            builtin_max = max(my_array.array)

            # Report out some logging info
            print('\nMy list = ', my_array.my_list)
            print('Correct max = ', builtin_max == my_sum)
            print('Built-in Max: ', builtin_max)
            print('My Max: {}\n'.format(my_sum))

    def find_max(self):
        ret_sum = 0
        for val in self.array:
            ret_sum = ret_sum if ret_sum > int(val) else int(val)

        # Validation
        if self.verbose:
            self.validate_find_max()
        return ret_sum
