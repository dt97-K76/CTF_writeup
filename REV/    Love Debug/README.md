## Challenge Description 

If you send this to someone, you'll be dumped... unless it's someone who knows a thing or two about reverse engineering...

Side Note: A love letter is what inspired the author to become a hacker.

Author: drec

## Solution

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/32363034-714b-4422-8cf8-b57797e001d8)

![arrayAddr](https://github.com/datvn09/CTF_writeup/assets/157048397/c8a12d27-69e9-48c4-a5af-f48e9db2eabe)

```
gdb-gef

GEF for linux ready, type `gef' to start, `gef config' to configure
88 commands loaded and 5 functions added for GDB 12.1 in 0.00ms using Python engine 3.10
gef➤  file love-letter-for-you
Reading symbols from love-letter-for-you...
(No debugging symbols found in love-letter-for-you)
gef➤  r
Starting program: /mnt/c/Users/acer/Desktop/love-letter-for-you

     ❤️❤️❤️❤️❤️❤️       ❤️❤️❤️❤️❤️❤️
   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
 ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
 ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
      ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
        ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
           ❤️❤️❤️❤️❤️❤️❤️
             ❤️❤️❤️
              ❤️

Are you amazed? You like it? Say something!
You're just here for the flag, are you?
```

![readAddr](https://github.com/datvn09/CTF_writeup/assets/157048397/c1b99423-779b-4609-a9cc-a21b6d25d46f)


source code solution

```
import gdb
import re

file = "love-letter-for-you"
with open('temp', 'wb') as f:
    f.write(b'\x03')
gdb.execute("file {}".format(file))
readAddr = 0x404272
gdb.execute(f"b *{readAddr}")
arrayAddr = 0x406000
arraySize = 30000
gdb.execute("r < temp")
gdb.execute(f"dump memory {file}-dump {hex(arrayAddr)} {hex(arrayAddr + arraySize)}")

with open(f"{file}-dump", 'rb') as f:
    dump = f.read().replace(b'\x00', b'')

match = re.search(b'uoftctf{(.+?)}', dump)
print(match.group(0).decode())

gdb.execute("q")

```
