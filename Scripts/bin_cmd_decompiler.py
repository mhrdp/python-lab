import argparse
import os
import struct
import sys

my_parser = argparse.ArgumentParser(
    # Rewrite the name of the program at runtime
    prog = 'test-cmd',

    description = 'List the content of the folder',
    fromfile_prefix_chars = '@',
    usage = '%(prog)s [option] path',
    allow_abbrev = False,
)

my_parser.add_argument(
    '--int', 
    action = 'store', 
    type = int, 
    help = 'Input any kind of integer', 
    required = False,
)
my_parser.add_argument(
    '--d',
    help = 'Input .bin file to be read',
    required = False,
)

args = my_parser.parse_args()

if sys.argv[1] == '--int':
    print(args.int)

if sys.arv[1] == '--d':
    with open(args.d, 'rb') as f:
        readbin = f.read()

    struct.unpack('i' * ((len(readbin) -24) // 4), readbin[20:-4])

