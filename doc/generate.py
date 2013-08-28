#!/usr/bin/env python

from __future__ import print_function
from collections import OrderedDict


def load_codes(file_name):
    codes = {}

    for line in open(file_name, 'r'):
        if not line:
            continue
        try:
            code, torque_name = line.strip().split(None, 1)
        except:
            print('Invalid line: %s' % line)
            continue

        codes[code] = torque_name

    return codes


def write_table(codes):
    sorted_codes = OrderedDict(sorted(codes.items(), key=lambda x: x[1]))
    max_code_length = 6
    max_qs_length = max_code_length + 1
    max_name_length = len(max(codes.values(), key=len))
    torque_prefixes = ['fe', 'ff']

    format = '| %%-%ss   |  %%%ss |  %%%ss |' % (max_name_length,
                                                 max_code_length,
                                                 max_qs_length)
    for code, torque_name in sorted_codes.iteritems():
        qs_code = 'k' + code
        is_custom = (len(code) == 6 and code[0:2] in torque_prefixes)
        code = '' if is_custom else code

        print(format % (torque_name, code, qs_code))


if __name__ == '__main__':
    codes = load_codes('codes.in')
    write_table(codes)
