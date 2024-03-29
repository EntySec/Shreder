# Shreder

[![Developer](https://img.shields.io/badge/developer-EntySec-blue.svg)](https://entysec.com)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://github.com/EntySec/Shreder)
[![Forks](https://img.shields.io/github/forks/EntySec/Shreder?style=flat&color=green)](https://github.com/EntySec/Shreder/forks)
[![Stars](https://img.shields.io/github/stars/EntySec/Shreder?style=flat&color=yellow)](https://github.com/EntySec/Shreder/stargazers)
[![CodeFactor](https://www.codefactor.io/repository/github/EntySec/Shreder/badge)](https://www.codefactor.io/repository/github/EntySec/Shreder)

Shreder is a powerful multi-threaded SSH protocol password brute-force tool.

## Features

* Very fast password guessing, just one password in `0.1` second.
* Optimized for big password lists, Shreder tries 1000 passwords in `1` minute and `40` seconds.
* Simple CLI and API usage.

## Installation

```shell
pip3 install git+https://github.com/EntySec/Shreder
```

## Basic usage

To use Shreder just type `shreder` in your terminal.

```
usage: shreder [-h] [-p PORT] [-u USERNAME] [-l LIST] [-d DELAY] target

Shreder is a powerful multi-threaded SSH protocol password brute-force tool.

positional arguments:
  target

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  SSH port.
  -u USERNAME, --username USERNAME
                        SSH username.
  -l LIST, --list LIST  Passwords list.
  -d DELAY, --delay DELAY
                        Delay between login attempts.
```

### Examples

**Brute-forcing single target**

Let's brute-force my device just for fun.

```shell
shreder 192.168.2.109 -u mobile -l passwords.txt
```

## API usage

Shreder also has their own Python API that can be invoked by importing Shreder to your code.

```python
from shreder import Shreder
```

### Basic functions

There are all Shreder basic functions that can be used to brute-force single target.

* `connect(host, port, username, password)` - Connect single target by given address.
* `brute(host, port, username, dictionary, delay)` - Brute-force single target by given address.

### Examples

**Brute-forcing single target**

```python
from shreder import Shreder

shreder = Shreder()
password = shreder.brute('192.168.2.109', 22, 'mobile', 'passwords.txt')

print(password)
```
