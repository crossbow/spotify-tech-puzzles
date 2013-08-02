#!/usr/bin/env python

"""
Reverse integer number in binary. 
For instance, the binary representation of 13 is 1101, 
and reversing it gives 1011, which corresponds to number 11.

The input contains a single line with an integer N, 1 <= N <= 1000000000.

The output one line with one integer, the number 
we get by reversing the binary representation of N.
"""

def int_to_binary(int_number):
    """ Convert an integer to binary string format. """
    return bin(int_number)[2:]


def reverse_binary(binary_str):
    """ Reverse a binary string. """
    return ''.join(reversed(binary_str))

    
def binary_to_int(binary_str):
    """ Convert a binary string to int """
    return int(binary_str, 2)


def main():
    msg = "Please type an integer N, 1 <= N <= 1000000000"
    while True:
        try:
            n = input()
            if isinstance(n, int):
                if 1 <= n <= 1000000000:
                    break
        except:
            print msg
            continue
        else:
            print msg
    
    binary_str = int_to_binary(n)
    reversed_binary_str = reverse_binary(binary_str)
    result = binary_to_int(reversed_binary_str)
    #result = binary_to_int(reverse_binary(int_to_binary(n)))
    print result

if __name__ == '__main__':
    main()