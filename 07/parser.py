from typing import Optional

CONSTANT_TEMPLATE = '''
@{index}
D=A

@SP
A=M
M=D

@SP
M=M+1
'''

LCL_ARG_THIS_THAT_TEMPLATE_PUSH = '''
@{index}
D=A

@{segment}
A=M+D
D=A

@R13
M=D

@R13
A=M
D=M

@SP
M=M+1
A=M-1
M=D
'''

LCL_ARG_THIS_THAT_TEMPLATE_POP = '''
@{index}
D=A

@{segment}
A=M+D
D=A

@R13
M=D

@SP
AM=M-1
D=M

@R13
A=M
M=D
'''

TEMP_TEMPLATE_PUSH = '''
@{index}
D=A

@R5
A=A+D
D=A

@R14
M=D
A=M
D=M

@SP
M=M+1
A=M-1
M=D
'''


TEMP_TEMPLATE_POP = '''
@{index}
D=A

@R5
A=A+D
D=A

@SP
AM=M-1
D=M

@R14
A=M
M=D
'''


STATIC_TEMPLATE_PUSH = '''
@Foo.{index}
D=M

@SP
M=M+1
A=M-1
M=D
'''

STATIC_TEMPLATE_POP = '''
@SP
AM=M-1
D=M

@Foo.{index}
M=D
'''


POINTER_TEMPLATE_PUSH = '''
@{this_or_that}
D=M

@SP
M=M+1
A=M-1
M=D
'''

POINTER_TEMPLATE_POP = '''
@SP
AM=M-1
D=M

@{this_or_that}
M=D
'''

EQ_TEMPLATE = '''
@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere1
D;JEQ

@SP
A=M
M=0

(JumpHere1)
@SP
A=M
M=-1
'''

GT_TEMPLATE = '''
@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere2
D;JLT

@SP
A=M
M=0

(JumpHere2)
@SP
A=M
M=-1
'''

LT_TEMPLATE = '''
@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere3
A=M
D;JGT

@SP
A=M
M=0

(JumpHere3)
@SP
A=M
M=-1
'''

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
    jump_table = {}
    dest_table = {}
    compute_table = {
        'eq': EQ_TEMPLATE,
        'lt': LT_TEMPLATE,
        'gt': GT_TEMPLATE,
        'add': ADD_SUB_AND_OR_TEMPLATE.format('+'),
        'sub': ADD_SUB_AND_OR_TEMPLATE.format('-'),
        'and': ADD_SUB_AND_OR_TEMPLATE.format('&'),
        'or': ADD_SUB_AND_OR_TEMPLATE.format('|'),
        'neg': NOT_NEG_TEMPLATE.format('-'),
        'not': NOT_NEG_TEMPLATE.format('!'),
    }
    segment_mapping = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
    }
    map = {
        'constant': {'push': CONSTANT_TEMPLATE},
        'static': {'push': STATIC_TEMPLATE_PUSH, 'pop': STATIC_TEMPLATE_POP},
        'temp': {'push': TEMP_TEMPLATE_PUSH, 'pop': TEMP_TEMPLATE_POP},
        'pointer': {'push': POINTER_TEMPLATE_PUSH, 'pop': POINTER_TEMPLATE_POP},
        'local': {'push': LCL_ARG_THIS_THAT_TEMPLATE_PUSH, 'pop': LCL_ARG_THIS_THAT_TEMPLATE_POP},
        'argument': {'push': LCL_ARG_THIS_THAT_TEMPLATE_PUSH, 'pop': LCL_ARG_THIS_THAT_TEMPLATE_POP},
        'this': {'push': LCL_ARG_THIS_THAT_TEMPLATE_PUSH, 'pop': LCL_ARG_THIS_THAT_TEMPLATE_POP},
        'that': {'push': LCL_ARG_THIS_THAT_TEMPLATE_PUSH, 'pop': LCL_ARG_THIS_THAT_TEMPLATE_POP},
    }

    @classmethod
    def parse(cls, line: str) -> Optional[str]:
        line = line.strip()
        if not line or line.startswith('//'):
            return
        parts = line.split()
        line_words = len(parts)
        if line_words not in (1, 3):
            raise ValueError(f'wrong line format {line}')
        elif len(parts) == 1:
            return cls.compute_table[parts[0]]
        else:
            stack_operation, segment, index = parts
            return cls.get_template_for_segment(segment=segment, stack_operation=stack_operation, index=index)

    @classmethod
    def get_template_for_segment(cls, segment, index, stack_operation):
        try:
            template = cls.map[segment][stack_operation]
        except KeyError:
            raise ValueError(f'wrong line format {stack_operation, segment, index}')
        if segment in ('local', 'argument', 'this', 'that'):
            hack_segment = cls.segment_mapping[segment]
            return template.format(index=index, segment=hack_segment)
        elif segment == 'pointer':
            return template.format(this_or_that='THIS' if index == '0' else 'THAT')
        return template.format(index=index)
