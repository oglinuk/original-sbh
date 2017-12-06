# SaltBaeHash

## Security through obscurity - Learn more about [ciphers](https://en.wikipedia.org/wiki/Cipher)

### Next level of password security
#### Plain text ->
#### n(0 < n < infinity) cipher(s) applied ->
#### n(0 < n < infinity) rotation(s) ->
#### n(0 < n < infinity) amount of potential hashs ->
#### store in a password manager if needed

# How to use

1. ```python run.py``` (windows) or ```python3 run.py``` (linux)
2. enter a plain text - it is important to note that capitalization produces a different hash
3. enter a number of [caesar ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) that you want to apply
4. enter a number for the rotation applied to each character of the plain text
5. store the hash in a [password manager](https://www.lastpass.com/) or remember the cipher number and rotation pattern

## Example

Plain text: steam
N of Ciphers: 5
Rotation 1: 2
Rotation 2: 3
Rotation 3: 5
Rotation 4: 7
Rotation 5: 11
SaltBaeHash: 311dac1512a811e898a950bf4a478c383b1227775d948dc33130659d785f7a99

# Installation

Install [Windows Python 3.6.3](https://www.python.org/ftp/python/3.6.3/Python-3.6.3.exe)

Linux has both Python3 and Python2 installed by default, so you might just need to update to the latest version of Python3.

<hr>

Install [Windows Git](https://github.com/git-for-windows/git/releases/download/v2.15.0.windows.1/Git-2.15.0-64-bit.exe)

or

```
sudo apt install git -y
```

<hr>

<b>To clone the program</b>
```
git clone https://github.com/OGLinuk/sbh.git
```

Navigate to where you cloned SaltBaeHash in cmd or terminal
* If youre on windows the command to start sbh is python run.py
* If youre on Linux the command to start sbh is python3 run.py

## Benefits
* Free
* Easy to use
* <b><i>Very</i></b> secure

## Milestones

* Add the ability to apply an automation to the assignment
of the rotations which could be stored as say a private key. This would make number of ciphers 2 < digits easier to use
* Add more cipher methods as options
* Add the option to generate sha512 hashs rather than sha256
* Add sbh layer to PGP encryption(keybase)
* Executable
