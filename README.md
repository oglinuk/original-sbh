# SaltBaeHash

## Security through obscurity

### Learn more about [ciphers](https://en.wikipedia.org/wiki/Cipher) || [hash functions](https://en.wikipedia.org/wiki/Hash_function)

# How to use

1. ```python run.py``` (windows) || ```python3 run.py``` (linux)
2. Input a plain text - it is important to note that capitalization produces a different hash
3. Input a number of [caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) that you want to apply
4. Input a seed

# Example
```
-----------------Salt Bae Hash-----------------
Plain Text -> Cipher(s) -> Hash(s)
Plain Text: test
Num of ciphers: 1729
Seed: 42
Salt Bae Encrypted String: 3555c82d3104b27623438398a1044099315ff62ea2c389de35e4d542be1930d1

Press enter to sbh another plain text input ...
```

# Installation

Install [Windows Python 3.6.3](https://www.python.org/ftp/python/3.6.3/Python-3.6.3.exe) | Linux has Python3 installed by default

Install [Git](https://github.com/git-for-windows/git/releases/download/v2.15.0.windows.1/Git-2.15.0-64-bit.exe) (windows) | ```sudo apt install git -y``` (linux)

<b>To clone the program</b> - ```git clone https://github.com/OGLinuk/sbh.git``` || click the [download](https://github.com/OGLinuk/sbh/archive/master.zip) button

# Benefits
* Free
* Easy to use
* <b><i>Very</i></b> secure

# Milestones
* Add more cipher methods as options
* Add the option to generate sha512 hashs rather than sha256
* Make into executable
* Dockerize
