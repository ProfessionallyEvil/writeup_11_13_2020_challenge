#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Program: multi-arch-dump.py

Date: 11/24/2020

Author: Travis Phillips

Website: https://github.com/ProfessionallyEvil/writeup_11_13_2020_challenge

Purpose: A simple script that will take an argument in as a file path
         and will run it through a loop that will attempt to dump the
         disassembly for it on multiple architectures.

""" 
import sys
from pwn import *

def main(args):
    """ Main program logic """
    # Check that the user provided an argument or print usage.
    if len(args) != 2:
        print("\n\t[*] Usage: {0:s} [bin_file]\n".format(args[0]))
        return 1

    # Get the payload binary data.
    with open(args[1], 'rb') as fil:
        payload_data = fil.read()
    
    log.info("Payload size: {0:d}".format(len(payload_data)))
    log.info("Payload hexdump:")
    print(hexdump(payload_data))

    # Run the payload through the disassembly Gauntlet.
    for key, val in pwnlib.context.ContextType.architectures.items():
        print("\n\t..::[ Disassembly as {0:s} ]::..\n".format(key))
        with context.local(arch = key):
            try:
                print(disasm(payload_data))
            except pwnlib.exception.PwnlibException as e:
                log.failure(e)
            except Exception as e:
                log.failure(e)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
