import itertools
import re
from functools import partial

LABEL_REGEX = re.compile(r'\((.+)\)')
VAR_REGEX = re.compile(r'@(.+)')
strip_comments = partial(re.sub, r'\/\/.+', '')

CONSTANT_TEMPLATE = f'''
@{index}
D=A

@SP
A=M
M=D

@SP
M=M+1
'''


LCL_ARG_THIS_THAT_TEMPLATE = f'''
@{index}
D=A

@{PLACE}
A=M
M=D+M

@SP
AM=M{PLUS_MINUS}1
D=M

@{PLACE}
M=D
'''

EQ_TEMPLATE = ''''''

class ValidationError(Exception):
    pass


class VMParser:
    symbol_table = {'SCREEN': '16384', 'KBD': '24576'}
    jump_table = {}
    dest_table = {}
    compute_table = {
        'eq': EQ_TEMPLATE,
        'lt': EQ_TEMPLATE,
        'gt': EQ_TEMPLATE,
        'add': EQ_TEMPLATE,
        'sub': EQ_TEMPLATE,
        'neg': EQ_TEMPLATE,
        'and': EQ_TEMPLATE,
        'or': EQ_TEMPLATE,
        'not': EQ_TEMPLATE,
    }

    def parse(self, line):
        parts = line.split()
        if len(parts) == 3:
            stack_operation, segment, index = parts
        elif len(parts) == 1:
            template = self.compute_table[parts[0]]
        else:
            raise ValueError(f'wrong line format {line}')
