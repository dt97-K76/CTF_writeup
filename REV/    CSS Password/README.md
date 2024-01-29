## Challenge Description 

My web developer friend said JavaScript is insecure so he made a password vault with CSS. Can you find the password to open the vault?

Wrap the flag in uoftctf{}

Make sure to use a browser that supports the CSS :has selector, such as Firefox 121+ or Chrome 105+. The challenge is verified to work for Firefox 121.0.

Author: notnotpuns

## Solution

![FlagChecker](https://github.com/datvn09/CTF_writeup/assets/157048397/1bf0cffd-73c1-405e-87d7-868dd8f4c526)

```
import re

pattern = re.compile(
    r'.wrapper:has\(\.byte:nth-child\((\d+)\) \.latch:nth-child\((\d+)\) \.latch__(\w+):active\) .checker:nth-of-type\((\d+)\) .checker__state:nth-child\((\d+)\) {\n\s+transform: translateX\(([-\d]+)%\);\n\s+transition: transform 0s;')

text = open("css-password.html").read()
matches = pattern.findall(text)

bin = [[0] * 8 for _ in range(19)]
for match in matches:
    if match[2] == "set":
        byteNo = int(match[0])
        latchNo = int(match[1])
        binary = match[5]
        (bin[byteNo-1])[latchNo-1] = 1 if binary == "-100" else 0

for _ in bin:
    print(chr(int(''.join(map(str, _)),2)),end="")

# Flag: uoftctf{CsS_l0g1c_is_fun_3h}
```
