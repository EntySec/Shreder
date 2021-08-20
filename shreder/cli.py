#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import time
import argparse

from .__main__ import Shreder
from .badges import Badges


class ShrederCLI(Shreder, Badges):
    description = "Shreder is a powerful multi-threaded SSH protocol password brute-force tool."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('target')
    parser.add_argument('-p', '--port', dest='port', help='SSH port.')
    parser.add_argument('-u', '--username', dest='username', help='SSH username.')
    parser.add_argument('-l', '--list', dest='list', help='Passwords list.')
    parser.add_argument('-d', '--delay', dest='delay', help='Delay between login attempts.')
    args = parser.parse_args()

    def start(self):
        if self.args.target and self.args.username and self.args.list:
            if not os.path.exists(self.args.list):
                self.print_error(f"List file: {self.args.input}: does not exist!")
                return

            if not self.args.port:
                self.args.port = 22

            start = time.time()
            password = self.brute(
                self.args.target,
                self.args.port,
                self.args.username,
                self.args.list,
                float(self.args.delay) if self.args.delay else 0.1
            )
            end = time.time()

            if password:
                self.print_success("Password has been found!")
                self.print_information(f"Password: {password}")
            else:
                self.print_warning("Password is not found.")
            self.print_information(f"Time elapsed: {str(end - start)}")
        else:
            self.parser.print_help()

def main():
    cli = ShrederCLI()
    cli.start()
