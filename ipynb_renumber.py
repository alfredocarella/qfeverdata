#!/usr/bin/env python

"""
Consecutively renumber prompts in an IPython notebook.
"""

# Copyright (c) 2015, Lev Givon
# All rights reserved.
# Distributed under the terms of the BSD license:
# http://www.opensource.org/licenses/bsd-license

import argparse
import simplejson

def renumber(data):
    """
    Consecutively renumbers prompts in IPython notebook data.
    """

    # Unserialize:
    d = simplejson.loads(data)

    if d['nbformat'] < 4:
        raise RuntimeError('Can only renumber notebooks with format 4 or later')

    prompt_num = 1
    for cell in d['cells']:
        if cell['cell_type'] == 'code':
            cell['execution_count'] = prompt_num
            if 'outputs' in cell:
                for out in cell['outputs']:
                    out['execution_count'] = prompt_num
            prompt_num += 1

    # Reserialize:
    return simplejson.dumps(d, indent=' ')

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file')
parser.add_argument('output_file', help='Output file')
args = parser.parse_args()

with open(args.input_file, 'r') as fi, \
     open(args.output_file, 'w') as fo:
    fo.write(renumber(fi.read()))
