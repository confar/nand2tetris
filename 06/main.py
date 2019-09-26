import argparse
import os

from parser import AssemblyParser


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assemly the hack machine code')
    parser.add_argument('infile', type=str, help='Input file for hack code')
    parser.add_argument('outfile', type=str, help='Output file for binary assembled code')

    args = parser.parse_args()
    infile = os.path.join(os.getcwd(), args.infile)
    if not os.path.exists(infile):
        raise FileNotFoundError(f'file {infile} was not found in the current directory')
    assembly_parser = AssemblyParser(infile)
    assembly_parser.parse()

    outfile = os.path.join(os.getcwd(), args.outfile)
    with open(outfile, 'w') as out:
        out.write('\n'.join(assembly_parser.lines_to_write))
