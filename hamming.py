# this method is from https://en.wikipedia.org/wiki/Hamming_distance
def string_hamming_distance(string1, string2):
    dist_counter = 0
    for n in range(len(string1)):
        if string1[n] != string2[n]:
            dist_counter += 1
    return dist_counter


# assume strings are same length and limited to given alphabet
def binary_hamming_distance(string1, string2):
    b1 = string_to_hamming_binary(string1)
    b2 = string_to_hamming_binary(string2)
    return binary_hamming_dist_calc(b1, b2)


def binary_hamming_dist_calc(binary1, binary2):
    return bit_count(binary1 ^ binary2) / 2


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


# assumes strings only contain given alphabet
def string_to_hamming_binary(text):
    result = 0
    for c in text:
        result = result << 4  # left bitshift 4 characters
        result += char_to_hamming_binary(c)
    return result


# from https://wiki.python.org/moin/BitManipulation
# from an algorithm published by Peter Wegner in CACM 3 (1960)
def bit_count(number):
    count = 0
    while number:
        number &= number - 1
        count += 1
    return count
