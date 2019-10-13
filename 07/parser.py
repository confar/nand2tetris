TEMP_START_MEMORY = 5

CONSTANT_TEMPLATE = '''
@{index}
D=A

@SP
A=M
M=D

@SP
M=M+1
'''

LCL_ARG_THIS_THAT_TEMPLATE = '''
@{index}
D=A

@{segment}
A=M+D
D=A

@R13
M=D

@SP
AM=M{stack_operation}1
D=M

@R13
A=M
M=D
'''

TEMP_TEMPLATE = '''
@{index}
D=A

@R5
A=A+D
D=A

@R14
M=D

@SP
AM=M{stack_operation}1
D=M

@R14
A=M
M=D
'''


STATIC_TEMPLATE = '''
'''


POINTER_TEMPLATE = '''
'''

EQ_TEMPLATE = ''''''

ADD_SUB_AND_OR_TEMPLATE = '''
@SP
AM=M-1
D=M

@SP
A=M-1
M=M{}D

'''

NOT_NEG_TEMPLATE = '''
@SP
M={}M
'''


class ValidationError(Exception):
    pass


class VMParser:
    symbol_table = {'SCREEN': '16384', 'KBD': '24576'}
    jump_table = {}
    dest_table = {}
    compute_table = {
        # 'eq': EQ_TEMPLATE,
        # 'lt': EQ_TEMPLATE,
        # 'gt': EQ_TEMPLATE,
        'add': ADD_SUB_AND_OR_TEMPLATE.format('+'),
        'sub': ADD_SUB_AND_OR_TEMPLATE.format('-'),
        'neg': NOT_NEG_TEMPLATE.format('-'),
        'and': ADD_SUB_AND_OR_TEMPLATE.format('&'),
        'or': ADD_SUB_AND_OR_TEMPLATE.format('|'),
        'not': NOT_NEG_TEMPLATE.format('!'),
    }
    var_table = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
    }

    @classmethod
    def parse(cls, line: str) -> str:
        line = line.strip()
        if not line or line.startswith('//'):
            return
        parts = line.split()
        if len(parts) == 3:
            stack_operation, segment, index = parts
            if segment in ('local', 'argument', 'this', 'that'):
                segment = cls.map_segment_to_var(segment)
                to_write = LCL_ARG_THIS_THAT_TEMPLATE.format(
                    index=index, segment=segment, stack_operation='+' if stack_operation == 'push' else '-')
            elif segment == 'constant':
                to_write = CONSTANT_TEMPLATE.format(index=index)
            elif segment == 'temp':
                to_write = TEMP_TEMPLATE.format(index=index,
                                                stack_operation='+' if stack_operation == 'push' else '-')
            else:
                to_write = ''
        elif len(parts) == 1:
            to_write = cls.compute_table[parts[0]]
        else:
            raise ValueError(f'wrong line format {line}')
        return to_write

    @classmethod
    def map_segment_to_var(cls, segment):
        return cls.var_table[segment]
