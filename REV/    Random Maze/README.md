## Challenge Description 

a little maze for you! just don't get lost! :3 remember, if you end up somewhere that doesn't look right, it probably isn't!

free hint: the entire flag is lower-alphanumeric ASCII.

Author: cartoonraccoon

## Solution

Dịch ngược tệp thực thi đã cho. Trong chức năng chính, bạn sẽ tìm thấy phương pháp lọc đầu vào đầu tiên.

![pass1](https://github.com/datvn09/CTF_writeup/assets/157048397/82b73296-6d83-4822-abb6-b2017c867979)

Từ dòng đó, chúng ta biết rằng đầu vào của người dùng phải lớn hơn hoặc bằng 19 và nhỏ hơn 100 (trong ASCII). Mỗi ký tự trong đầu vào cũng không được là bội số của 3 [a == 3 * (a / 3)] và 4 [a & 3 != 0]

![pass2](https://github.com/datvn09/CTF_writeup/assets/157048397/4fb2538b-454e-4e81-8026-4f362d739ec8)

### Code
```
from Crypto.Util.number import isPrime

sum = [0xCE, 0xA1, 0xAE, 0xAD, 0x64, 0x9F, 0xD5]
enc_flag = "ON#X~o8&"
list_Prime = []
for i in range (19, 100):
    if (isPrime(ord(enc_flag[0]) ^ i) and (i & 3 != 0) and (i%3!=0) ):
        list_Prime.append(i)
print (list_Prime)

for i in range (len(list_Prime)):
    list_Prime[i]=list_Prime[i]^ord(enc_flag[0])
print(list_Prime)

for i in range(len(list_Prime)):
    x = list_Prime[i]
    flag=""
    flag+=chr(x)
    j = (sum[0] - x)
    flag+=chr(j)
    for i in range (2,8):
        j = ((sum[i-1] - j))
        flag+=chr(j)
    if flag.isalnum() and flag.islower():
        print(flag)
        break
```

