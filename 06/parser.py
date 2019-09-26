import itertools
import re
from functools import partial

LABEL_REGEX = re.compile(r'\((.+)\)')
VAR_REGEX = re.compile(r'@(.+)')
strip_comments = partial(re.sub, r'\/\/.+', '')


class ValidationError(Exception):
    pass


class AssemblyParser:
    symbol_table = {'SCREEN': '16384', 'KBD': '24576'}
    jump_table = {}
    dest_table = {}
    compute_table = {
        '0': ('101010', '0'),
        '1': ('111111', '0'),
        '-1': ('111010', '0'),
        'D': ('001100', '0'),
        'A': ('110000', '0'),
        '!D': ('001101', '0'),
        '!A': ('110001', '0'),
        '-D': ('001111', '0'),
        '-A': ('110011', '0'),
        'D+1': ('011111', '0'),
        'A+1': ('110111', '0'),
        'D-1': ('001110', '0'),
        'A-1': ('110010', '0'),
        'D+A': ('000010', '0'),
        'D-A': ('010011', '0'),
        'A-D': ('000111', '0'),
        'D&A': ('000000', '0'),
        'D|A': ('010101', '0'),

        'M': ('110000', '1'),
        '!M': ('110001', '1'),
        '-M': ('1100011', '1'),
        'M+1': ('110111', '1'),
        'M-1': ('110010', '1'),
        'D+M': ('000010', '1'),
        'D-M': ('010011', '1'),
        'M-D': ('000111', '1'),
        'D&M': ('000000', '1'),
        'D|M': ('010101', '1')
    }

    def __init__(self, filename):
        self.fill_predefined_symbols()
        with open(filename) as f:
            self.file = f.readlines()
        self.fill_variables_and_labels()
        self.lines_to_write = []

    def fill_predefined_symbols(self):
        for i in range(16):
            self.symbol_table[f'R{i}'] = str(i)

        for idx, val in enumerate(('SP', 'LCL', 'ARG', 'THIS', 'THAT')):
            self.symbol_table[val] = str(idx)

        binary_nums_8bit = [''.join(i) for i in itertools.product('01', repeat=3)][1:]
        for dest, jump, binary in zip(('M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD'),
                                      ('JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP'),
                                      binary_nums_8bit):
            self.jump_table[jump] = binary
            self.dest_table[dest] = binary

    def parse(self):
        idx = 0
        var_counter = 16
        for line in self.file:
            line = strip_comments(line)
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            elif line.startswith('@'):  # A instruction or variable
                variable_or_a = self.clean_line_with_regex(line, regex=VAR_REGEX)
                if variable_or_a.isdigit():
                    a_instruction = f'0{int(variable_or_a):015b}'
                    self.lines_to_write.append(a_instruction)
                else:
                    if variable_or_a not in self.symbol_table:
                        self.symbol_table[variable_or_a] = str(var_counter)
                        print(variable_or_a)
                        var_counter += 1
                    value = self.symbol_table.get(variable_or_a)
                    a_instruction = f'0{int(value):015b}'
                    self.lines_to_write.append(a_instruction)
            elif ';' in line:  # C instruction with jump
                LHS, RHS = line.split(';')
                jump_bits = self.jump_table.get(RHS)
                compute_bits, a = self.compute_table.get(LHS)
                c_instruction = f'111{a}{compute_bits}000{jump_bits}'
                self.lines_to_write.append(c_instruction)
            elif '=' in line:  # C instruction
                LHS, RHS = line.split('=')
                dest_bits = self.dest_table.get(LHS)
                compute_bits, a = self.compute_table.get(RHS)
                c_instruction = f'111{a}{compute_bits}{dest_bits}000'
                self.lines_to_write.append(c_instruction)
            idx += 1
        print(self.symbol_table)

    def clean_line_with_regex(self, line, regex):
        matches = regex.findall(line)
        if matches:
            return matches[0]

    def fill_variables_and_labels(self):
        idx = 0
        for line in self.file:
            line = strip_comments(line)
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            if line.startswith('('):  # label
                label = self.clean_line_with_regex(line, regex=LABEL_REGEX)
                if not label:
                    raise ValidationError(f'Label is not with proper attributes for line {line} idx {idx}')
                if label not in self.symbol_table:
                    self.symbol_table[label] = str(idx)
            else:
                idx += 1
