# Thanks to https://www.geeksforgeeks.org/timeit-python-examples/ for timing examples.
# importing the required modules
import timeit
import random

from hamming import string_hamming_distance, string_to_hamming_binary, binary_hamming_distance, binary_hamming_dist_calc
from hamming_max_dist import string_hamming_distance_max_stop, binary_hamming_distance_max_stop, \
    binary_hamming_dist_calc_max_stop, bit_count_max_stop


def string_generator(size=63, chars=None):
    if chars is None:
        chars = ['A', 'G', 'T', 'C']
    return ''.join(random.choice(chars) for _ in range(size))


# compute string hamming time
def string_time():
    SETUP_CODE = ''' 
from hamming import string_hamming_distance 
from random import choice
from __main__ import string_generator
list_of_strings1 = [string_generator() for i in range(10)]
list_of_strings2 = [string_generator() for i in range(10)]'''

    TEST_CODE = ''' 
s1 = choice(list_of_strings1)
s2 = choice(list_of_strings2)
string_hamming_distance(s1, s2)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('Standard hamming string search time: {}'.format(min(times)))


# compute binary hamming time
def binary_inc_proccessing_time():
    SETUP_CODE = ''' 
from hamming import binary_hamming_distance 
from random import choice
from __main__ import string_generator
list_of_strings1 = [string_generator() for i in range(10)]
list_of_strings2 = [string_generator() for i in range(10)]'''

    TEST_CODE = ''' 
s1 = choice(list_of_strings1)
s2 = choice(list_of_strings2)
binary_hamming_distance(s1, s2)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('Binary hamming string search time (including preprocessing): {}'.format(min(times)))


# compute binary hamming time (on preprocessed string to binaries)
def binary_preprocessed_time():
    length_of_strings = 63
    character_set = ['A', 'G', 'T', 'C']
    SETUP_CODE_PREPROCESSED_BINARY = f''' 
from hamming import string_to_hamming_binary, binary_hamming_dist_calc
from random import choice
from __main__ import string_generator
list_of_binary_strings1 = [string_to_hamming_binary(string_generator({length_of_strings},{character_set})) for i in range(10)]
list_of_binary_strings2 = [string_to_hamming_binary(string_generator({length_of_strings},{character_set})) for i in range(10)]'''

    TEST_CODE = ''' 
s1 = choice(list_of_binary_strings1)
s2 = choice(list_of_binary_strings2)
binary_hamming_dist_calc(s1, s2)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE_PREPROCESSED_BINARY,
                          stmt=TEST_CODE,
                          repeat=10,
                          number=10000)

    # printing minimum exec. time
    print('Binary hamming string search time (not including preprocessing): {}'.format(min(times)))


if __name__ == "__main__":
    string_time()
    binary_preprocessed_time()
    binary_inc_proccessing_time()
