# another version with maximum distance between strings to stop comparison after


# this method is from https://en.wikipedia.org/wiki/Hamming_distance
from hamming import string_to_hamming_binary


def naive_hamming_distance_max_stop(string1, string2, max_dist):
    dist_counter = 0
    for n in range(len(string1)):
        if string1[n] != string2[n]:
            dist_counter += 1
            if dist_counter == max_dist:
                return dist_counter
    return dist_counter


# assume strings are same length and limited to given alphabet
def hamming_distance_max_stop(string1, string2, max_dist):
    b1 = string_to_hamming_binary(string1)
    b2 = string_to_hamming_binary(string2)
    return binary_hamming_dist_calc_max_stop(b1, b2, max_dist)


# stop counting at max_dist differences
def binary_hamming_dist_calc_max_stop(binary1, binary2, max_dist):
    return bit_count_max_stop((binary1 ^ binary2), max_dist*2) / 2


# Could make generic for any alphabet
def char_to_hamming_binary(text):
    if text == 'A':
        return 0b0001
    if text == 'C':
        return 0b0010
    if text == 'G':
        return 0b0100
    if text == 'T':
        return 0b1000
    return 0


# from https://wiki.python.org/moin/BitManipulation
# from an algorithm published by Peter Wegner in CACM 3 (1960)
# stop counting if max bits reached
def bit_count_max_stop(number, max_bits):
    count = 0
    while (number > 0) & (count < max_bits):
        number &= number - 1
        count += 1
    return count
