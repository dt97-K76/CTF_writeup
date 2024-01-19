## Challenge Description
last time we had a worbler, it failed miserably and left everyone sad, and no one got their flags. now we have another one, maybe it'll work this time?

output:
```
                      _     _             
                     | |   | |            
  __      _____  _ __| |__ | | ___ _ __   
  \ \ /\ / / _ \| '__| '_ \| |/ _ \ '__|  
   \ V  V / (_) | |  | |_) | |  __/ |     
    \_/\_/ \___/|_|  |_.__/|_|\___|_|     
                                          
==========================================
Enter flag: *redacted*
Here's your flag:  a81c0750d48f0750
```
Author: cartoonraccoon

File: [worbler](https://github.com/datvn09/CTF_writeup/blob/main/REV/%20%20%20%20All%20Worbled%20Up/worbler) [Python Bytecode/opcodes]

## Solution 
Một dạng bài về Opcodes Python, tôi sẽ cố gắng học và tìm hiểu về nó để có thể đọc hiểu vào một ngày gần nhất còn bây giờ với sự giúp đỡ nhiệt tình từ người bạn yêu quý của mình - [Chat GPT](https://chat.openai.com/), anh ấy đã giúp tôi convert Opcodes Python sang mã Python bình thường [worbler.py](https://github.com/datvn09/CTF_writeup/edit/main/REV/%2520%2520%2520%20All%20Worbled%20Up/worbler.py). Một thứ dường như thật dễ dàng!

Từ dòng lệnh sau:
>re_pattern = re.compile('^uoftctf\\{([bdrw013]){9}\\}$')

ta biết được chuỗi kí tự cần tìm có format uoftctf{chuoi_9_ki_tu} với chuoi_9_ki_tu này được lấy từ các kí tự sau "bdrw013". Vì vậy ý tưởng để giải quyết thử thách này là tạo nên một tập hợp gồm tất cả các chuỗi có 9 kí tự được tạo bởi "bdrw013" và thực hiện brute force để tìm ra output thỏa đề bài đã cho.
[solution.py](https://github.com/datvn09/CTF_writeup/blob/main/REV/%20%20%20%20All%20Worbled%20Up/solution.py)
```
import re
from itertools import product

re_pattern = '^uoftctf\\{([bdrw013]){9}\\}$'
pattern = re.compile(re_pattern)

def worble(s):
    s1 = 5
    s2 = 31

    for n in range(len(s)):
        s1 = (s1 + ord(s[n]) + 7) % 65521
        s2 = (s1 * s2) % 65521
    return (s2 << 16) | s1

def shmorble(s):
    r = ''
    for i in range(len(s)):
        r += s[len(s) - 1 - i]
    return r

def blorble(a, b):
    return format(a, 'x') + format(b, 'x')

characters = "bdrw013"
all_combinations = [''.join(combination) for combination in product(characters, repeat=9)]
for combination in all_combinations:
    flag = "uoftctf{" + combination + "}"
    if pattern.match(flag):
        a = worble(flag)
        b = worble(flag[::-1])
        c = shmorble(blorble(a, b))
        if c == "a81c0750d48f0750"[::-1]:
            print(flag)
            break
    else:
        print("Incorrect format!")

# Flag = uoftctf{d3w0rb13d}
```

