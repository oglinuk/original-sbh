# SaltBaeHash

## Security through obscurity

### Learn more about [ciphers](https://en.wikipedia.org/wiki/Cipher) || [hash functions](https://en.wikipedia.org/wiki/Hash_function)

<hr>

### Next level of password security
#### Plain text ->
#### n(0 < n < infinity) cipher(s) applied ->
#### n(0 < n < infinity) rotation(s) ->
#### n(0 < n < infinity) amount of potential hashs ->
#### store in a password manager or remember num of ciphers/rotation pattern

<hr>

# How to use

## W/ CLI

1. ```python run.py [nCiphers] [plainText] [rot1] [rot2...]``` (windows) | ```python3 run.py [args]``` (linux)

## W/o CLI
1. ```python run.py``` (windows) or ```python3 run.py``` (linux)
2. input a number of [caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) that you want to apply
3. input a plain text - it is important to note that capitalization produces a different hash
4. input a number for the rotation applied to each character of the plain text

<hr>

# Example

## W/ CLI
* ```python run.py 5 steam 2 3 5 7 11``` (windows) | ```python3 run.py 5 steam 2 3 5 7 11``` (linux)

<hr>

## W/o CLI
* Number of Ciphers: 5
* Plain text: steam
* Rotation 1: 2
* Rotation 2: 3
* Rotation 3: 5
* Rotation 4: 7
* Rotation 5: 11
* SBH: 311dac1512a811e898a950bf4a478c383b1227775d948dc33130659d785f7a99

<hr>

# Installation

Install [Windows Python 3.6.3](https://www.python.org/ftp/python/3.6.3/Python-3.6.3.exe) | Linux has Python3 installed by default

<hr>

Install [Git](https://github.com/git-for-windows/git/releases/download/v2.15.0.windows.1/Git-2.15.0-64-bit.exe) (windows) | ```sudo apt install git -y``` (linux)

<hr>

<b>To clone the program</b> - ```git clone https://github.com/OGLinuk/sbh.git```

# Benefits
* Free
* Easy to use
* <b><i>Very</i></b> secure

<hr>

# Milestones
* Add the ability to apply an automation to the assignment
of the rotations which could be stored as say a private key. This would make number of ciphers 2 < digits easier to use
* Add more cipher methods as options
* Add the option to generate sha512 hashs rather than sha256
* Make into executable
