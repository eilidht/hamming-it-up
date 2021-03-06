import time
import unittest
from random import choice, randint

from hamming import naive_hamming_distance, string_to_hamming_binary, hamming_distance, binary_hamming_dist_calc, \
    hamming_distance_wildcards, naive_hamming_distance_wildcards,string_to_hamming_binary_array, scipy_binary_hamming_dist
from hamming_max_dist import naive_hamming_distance_max_stop, hamming_distance_max_stop, \
    binary_hamming_dist_calc_max_stop, bit_count_max_stop


CHARACTERS = ['A', 'G', 'T', 'C']

def string_generator(size=63, chars=None):
    if chars is None:
        chars = CHARACTERS
    return ''.join(choice(chars) for _ in range(size))

def string_mutator(original:str, number_of_mutations:int):
    mutated = original
    positions = []
    # for number of mutations
    for x in range(number_of_mutations):
        # select a random position
        pos = randint(0,len(mutated)-1)
        # check not mutating same position twice
        while pos in positions:
            pos = randint(0,len(mutated)-1)
        positions.append(pos)
        # select replacement character
        replace = mutated[pos]
        temp_char_set = []
        for char in CHARACTERS:
            if char != replace:
                temp_char_set.append(char)
        # replace
        mutated = mutated[:pos] + choice(temp_char_set) + mutated[pos + 1:]

    print(f'original string {original}')
    print(f'modified string {mutated}')
    return mutated

class MyTestCase(unittest.TestCase):

    def test_hamming_dist_same(self):
        s1 = 'CAT'
        s2 = 'CAT'
        expected_dist = 0
        actual_dist = naive_hamming_distance(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = hamming_distance(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = scipy_binary_hamming_dist(s1, s2)
        self.assertEqual(expected_dist, actual_dist)

    def test_hamming_dist_different(self):
        s1 = 'CAT'
        s2 = 'AAT'
        expected_dist = 1
        actual_dist = naive_hamming_distance(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = hamming_distance(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = scipy_binary_hamming_dist(s1, s2)
        self.assertEqual(expected_dist, actual_dist)

    def test_hamming_dist_all_different(self):
        s1 = 'CAT'
        s2 = 'GGG'
        expected_dist = 3
        actual_dist = naive_hamming_distance(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = hamming_distance(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = scipy_binary_hamming_dist(s1, s2)
        self.assertEqual(expected_dist, actual_dist)


    def test_hamming_dist_wildcard_match(self):
        s1 = "C**T"
        s2 = "CAAT"
        expected_dist = 0
        actual_dist = naive_hamming_distance_wildcards(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = hamming_distance_wildcards(s1, s2)
        self.assertEqual(expected_dist, actual_dist)


    def test_hamming_dist_wildcard_different(self):
        s1 = "C**T"
        s2 = "TAAT"
        expected_dist = 1
        actual_dist = naive_hamming_distance_wildcards(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = hamming_distance_wildcards(s1, s2)
        self.assertEqual(expected_dist, actual_dist)


    def test_hamming_dist_wildcard_all_different(self):
        s1 = "C**T"
        s2 = "AAAA"
        expected_dist = 2
        actual_dist = naive_hamming_distance_wildcards(s1, s2)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = hamming_distance_wildcards(s1, s2)
        self.assertEqual(expected_dist, actual_dist)


    def test_haystack_generator(self):
        string_length = 6
        expected_dist = 3
        haystack = string_generator(string_length)
        needle = string_mutator(haystack, expected_dist)
        actual_dist = naive_hamming_distance(needle, haystack)
        self.assertEqual(expected_dist, actual_dist)
        actual_dist = hamming_distance(needle, haystack)
        self.assertEqual(expected_dist, actual_dist)


    def test_hamming_dist_timing(self):
        list_of_strings = [string_generator() for i in range(10)]
        print(list_of_strings)

        string_result = []
        string_start = time.process_time_ns()
        for s1 in list_of_strings:
            for s2 in list_of_strings:
                string_result.append(naive_hamming_distance(s1, s2))
        string_end = time.process_time_ns()
        print(f'no of mismatches = {string_result}')
        print("string hamming: {:,}".format(string_end - string_start))

        binary_result = []
        binary_start = time.process_time_ns()
        for s1 in list_of_strings:
            for s2 in list_of_strings:
                binary_result.append(hamming_distance(s1, s2))
        binary_end = time.process_time_ns()
        print("binary hamming: {:,}".format(binary_end - binary_start))

        list_of_preprocessed_binaries = []
        for s in list_of_strings:
            list_of_preprocessed_binaries.append(string_to_hamming_binary(s))

        binary_result_pre = []
        binary_start_pre = time.process_time_ns()
        for s1 in list_of_preprocessed_binaries:
            for s2 in list_of_preprocessed_binaries:
                binary_result_pre.append(binary_hamming_dist_calc(s1, s2))
        binary_end_pre = time.process_time_ns()
        print("prepro hamming: {:,}".format(binary_end_pre - binary_start_pre))
        self.assertEqual(string_result, binary_result)
        self.assertEqual(binary_result_pre, binary_result)


    def test_hamming_dist_max_dist_timing(self):
        max_dist = 8
        list_of_strings = [string_generator() for i in range(100)]
        print(list_of_strings)

        string_result = []
        for s1 in list_of_strings:
            for s2 in list_of_strings:
                string_result.append(naive_hamming_distance(s1, s2))
        print(f"no of mismatches with no max dist = {string_result}")

        string_result = []
        string_start = time.process_time_ns()
        for s1 in list_of_strings:
            for s2 in list_of_strings:
                string_result.append(naive_hamming_distance_max_stop(s1, s2, max_dist))
        string_end = time.process_time_ns()
        print(f"no of mismatches = {string_result}")
        print("string hamming: {:,}".format(string_end - string_start))

        binary_result = []
        binary_start = time.process_time_ns()
        for s1 in list_of_strings:
            for s2 in list_of_strings:
                binary_result.append(hamming_distance_max_stop(s1, s2, max_dist))
        binary_end = time.process_time_ns()
        print("binary hamming: {:,}".format(binary_end - binary_start))

        list_of_preprocessed_binaries = []
        for s in list_of_strings:
            list_of_preprocessed_binaries.append(string_to_hamming_binary(s))

        binary_result_pre = []
        binary_start_pre = time.process_time_ns()
        for s1 in list_of_preprocessed_binaries:
            for s2 in list_of_preprocessed_binaries:
                binary_result_pre.append(binary_hamming_dist_calc_max_stop(s1, s2, max_dist))
        binary_end_pre = time.process_time_ns()
        print("prepro hamming: {:,}".format(binary_end_pre - binary_start_pre))
        print(f"string_result {string_result}")
        print(f"binary_result {binary_result}")
        print(f"binary_result_pre {binary_result_pre}")
        self.assertEqual(string_result, binary_result)
        self.assertEqual(binary_result_pre, binary_result)

    def test_bit_count_max_stop(self):
        self.assertEqual(1, bit_count_max_stop(0b0001, 2))
        self.assertEqual(2, bit_count_max_stop(0b0011, 2))
        self.assertEqual(2, bit_count_max_stop(0b0111, 2))

    def test_one_letter_to_binary(self):
        self.assertEqual(0b0000, string_to_hamming_binary('*'))
        self.assertEqual(0b0001, string_to_hamming_binary('A'))
        self.assertEqual(0b0010, string_to_hamming_binary('C'))
        self.assertEqual(0b0100, string_to_hamming_binary('G'))
        self.assertEqual(0b1000, string_to_hamming_binary('T'))
        self.assertEqual([0, 0, 0, 1], string_to_hamming_binary_array('A'))

    def test_two_letters_to_binary(self):
        self.assertEqual(0b00010001, string_to_hamming_binary('AA'))
        self.assertEqual(0b00101000, string_to_hamming_binary('CT'))
        self.assertEqual(0b01000001, string_to_hamming_binary('GA'))
        self.assertEqual(0b10000100, string_to_hamming_binary('TG'))
        self.assertEqual([1,0,0,0,0,1,0,0], string_to_hamming_binary_array('TG'))

    def test_long_string_to_binary(self):
        self.assertEqual(0b0100000100101000100000010001001010001000000100010010100010000001,
                         string_to_hamming_binary('GACTTAACTTAACTTA'))  # 16 chars

    def test_longer_string_to_binary(self):
        self.assertEqual(
            0b01000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001,
            string_to_hamming_binary('GACTTAACTTAACTTAGACTTAACTTAACTTA'))  # 32 chars

    def test_longerer_string_to_binary(self):
        self.assertEqual(
            0b0100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001,
            string_to_hamming_binary('GACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTA'))  # 64 chars

    def test_longererer_string_to_binary(self):
        self.assertEqual(
            0b01000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001,
            string_to_hamming_binary(
                'GACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTA'))  # 128 chars

    def test_longerererer_string_to_binary(self):
        self.assertEqual(
            0b0100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001010000010010100010000001000100101000100000010001001010001000000101000001001010001000000100010010100010000001000100101000100000010100000100101000100000010001001010001000000100010010100010000001,
            string_to_hamming_binary(
                'GACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTAGACTTAACTTAACTTA'))  # 256 chars


if __name__ == '__main__':
    unittest.main()
