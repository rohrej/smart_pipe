#!/usr/bin/env python3
#
# Copyright (c) 2021-2022, Justin P. Rohrer
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Program:      $Id: pipe.py 1551 2015-02-11 14:14:09Z jprohrer $
# Author:       Justin P. Rohrer <rohrej@gmail.com>
# Description:  Pipe data from input to output line-by-line, based on URI and
#               file extension semantics
#

__author__ = 'Justin P. Rohrer <rohrej@gmail.com>'
__copyright__ = 'Copyright (c) 2021-2022 Justin P. Rohrer'
__url__ = 'https://github.com/rohrej/smart_pipe'
__version__ = 1.0

import sys
import argparse
import warnings
from smart_open import open


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pipe data to/from files based on URI and file extension.')
    parser.add_argument('infile', default='-', help='Input')
    parser.add_argument('outfile', default='-', help='Output')
    args = parser.parse_args()

    if args.infile == '-':
        input = sys.stdin
    else :
        input = open(args.infile)
    if args.outfile == '-':
        output = sys.stdout
    else :
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output = open(args.outfile, 'w')

    bytes_written = 0
    linebuf = ''
    linenum = 1
    for line in input:
        linebuf += line
        if linenum % 100 == 0:
            bytes_written += output.write(linebuf)
            linebuf = ''

        linenum += 1

    bytes_written += output.write(linebuf)

    print("Wrote", bytes_written, "bytes")

    output.close()

