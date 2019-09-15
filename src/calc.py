#!/usr/bin/env python3
"""Calculator program intended to solve all your difficult arithmetical
challenges!

Written according to the PEP-8 Style Guide
"""

# Import system modules
import argparse

# Import user modules
import my_function

# Acquire two numbers from the command line
PARSER = argparse.ArgumentParser(description='Grab some numbers')
PARSER.add_argument('number', type=int, nargs=2,
                    help='two numbers to be processed')

ARGS = PARSER.parse_args()

# Add the two numbers
result = my_function.add_integers(ARGS.number[0], ARGS.number[1])

# Print out the result
print("Answer: {:d}".format(result))
