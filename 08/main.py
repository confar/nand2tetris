import argparse
import os

from parser import VMParser
from parser import INIT_CODE


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate VM code to Hack machine language')
    parser.add_argument('infile', type=str, help='Input file for VM code')
    parser.add_argument('outfile', type=str, help='Output file for Hack ML code')

    args = parser.parse_args()
    infile = os.path.join(os.getcwd(), args.infile)
    if not os.path.exists(infile):
        raise FileNotFoundError(f'file {infile} was not found in the current directory')
    with open(infile) as to_read,  open(args.outfile, 'w') as to_write:
        for counter, line in enumerate(to_read):
            hack_code = VMParser.parse(line, counter)
            if hack_code:
                # write comment first
                to_write.write(f'// {line}')
                to_write.write(f'{hack_code}\n')
