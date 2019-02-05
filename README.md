# SaltBaeHash

## Security through obscurity

### Learn more about [ciphers](https://en.wikipedia.org/wiki/Cipher) || [hash functions](https://en.wikipedia.org/wiki/Hash_function)

# How to use

1. ```python run.py``` (windows) || ```python3 run.py``` (linux)
2. Input a number of [caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) that you want to apply
3. Input a plain text - it is important to note that capitalization produces a different hash
4. For n of caesar ciphers input a rotation (this must be remembered)

# Example
```
-----------------Salt Bae Hash-----------------
Plain Text -> Cipher(s) -> Hash(s)
Plain Text: test
Num of ciphers: 8 
Rotation: 0
Rotation: 1 
Rotation: 0 
Rotation: 1
Rotation: 1
Rotation: 9
Rotation: 7
Rotation: 0
Salt Bae Encrypted String: ee4e6bad0e3d52683b53038e7d683cd9447f6f21eac26c11b692bf1fcdda8cf7

Press enter to sbh another plain text input ...
```

# Installation

Install [Windows Python 3.6.3](https://www.python.org/ftp/python/3.6.3/Python-3.6.3.exe) | Linux has Python3 installed by default

Install [Git](https://github.com/git-for-windows/git/releases/download/v2.15.0.windows.1/Git-2.15.0-64-bit.exe) (windows) | ```sudo apt install git -y``` (linux)

<b>To clone the program</b> - ```git clone https://github.com/OGLinuk/sbh.git``` || click the [download](https://github.com/OGLinuk/sbh/archive/master.zip) button

# Benefits
* Free
* Easy to use
* <b><i>Very</i></b> secure ~ (when I change it)

# Milestones
* Add more cipher methods as options
* Add the option to generate sha512 hashs rather than sha256
* Make into executable
* Dockerize
* convert to the aes file encryption with rng values for rots 
