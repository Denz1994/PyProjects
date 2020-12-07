# import numpy
import random

my_list = []
for num in range(10):
    # my_list.append(numpy.random.randint(0, 50))
    my_list.append(random.randint(0,50))

def find_max(num_list):
    ret_sum = 0
    iteration = 0
    for val in num_list:
        iteration += 1
        ret_sum = ret_sum if ret_sum > val else val

    print('Iterations = ', iteration)
    return ret_sum

print('\nMy list = ', my_list)

my_sum = find_max(my_list)
builtin_max = max(my_list)
print('Correct max = ', builtin_max == my_sum )
print('Max: ', builtin_max)
print('My Max: ', my_sum)
