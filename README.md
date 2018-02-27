# SaltBaeHash

## Security through obscurity

### Learn more about [ciphers](https://en.wikipedia.org/wiki/Cipher) || [hash functions](https://en.wikipedia.org/wiki/Hash_function)

### Next level of password security
#### Plain text ->
#### n(0 < n < infinity) cipher(s) applied ->
#### n(0 < n < infinity) generated rotation(s) ->
#### n(0 < n < infinity) amount of potential hashs ->
#### stores rotations in a .txt file with (context)\_rotation.txt as the name
#### [WARNING] THE TXT FILE IS NOT SECURE -> PLEASE ENCRYPT IT WITH A PRIVATE KEY [WARNING]

# How to use

## W/ CLI

1. ```python run.py [nCiphers] [plainText]``` (windows) || ```python3 run.py [nCiphers] [plainText]``` (linux)

## W/o CLI
1. ```python run.py``` (windows) || ```python3 run.py``` (linux)
2. input a number of [caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) that you want to apply
3. input a plain text - it is important to note that capitalization produces a different hash

# Example

## W/ CLI (generate)
* ```python run.py -g 5 steam``` (windows) || ```python3 -g run.py 5 steam``` (linux)
* ```Context: steam```

## W/o CLI (generate)
* ```Number of Ciphers: 5```
* ```Plain Text: steam```
* ```Context: steam```
* ```SBH: 9db0348486f86559c3e9c5b9456e46d7bc05ce2727b75903b411050086a5464b```

## W/ CLI (reproduce)
* ```python run.py -r steam_rotations.txt steam``` (windows) || ```python3 -r steam_rotations.txt steam``` (linux)

## W/o CLI (reproduce)
* ```Rotation File: steam_rotations.txt```
* ```Plain Text: steam```

# Installation

Install [Windows Python 3.6.3](https://www.python.org/ftp/python/3.6.3/Python-3.6.3.exe) | Linux has Python3 installed by default

Install [Git](https://github.com/git-for-windows/git/releases/download/v2.15.0.windows.1/Git-2.15.0-64-bit.exe) (windows) | ```sudo apt install git -y``` (linux)

<b>To clone the program</b> - ```git clone https://github.com/OGLinuk/sbh.git``` || click the [download](https://github.com/OGLinuk/sbh/archive/master.zip) button

# Benefits
* Free
* Easy to use
* <b><i>Very</i></b> secure

# Milestones
* Add the ability to apply an automation to the assignment
of the rotations which could be stored as say a private key. This would make number of ciphers 2 < digits easier to use
* Add more cipher methods as options
* Add the option to generate sha512 hashs rather than sha256
* Make into executable
