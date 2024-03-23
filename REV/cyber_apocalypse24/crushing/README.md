## Describe
`
You managed to intercept a message between two event organizers. Unfortunately, it's been compressed with their proprietary message transfer format. Luckily, they're gamemakers first and programmers second - can you break their encoding?

Author: clubby789
`

## Solution 

Đối với challenge này, tôi nhận được hai tệp. Một tệp nhị phân và một tệp có tên message.txt.cz chứa dữ liệu được mã hóa.

Mở tệp nhị phân với IDA và bắt đầu phân tích:



```
char_map = [[] for _ in range(255)]

with open("message.txt.cz", "rb") as file:
    for index in range(255):
        count = int.from_bytes(file.read(8), 'little')
        print(chr(index), count)
        if count != 0:
            for i in range(count):
                char_map[index].append(int.from_bytes(file.read(8), 'little'))

text = [' ']*900

for i in range(len(char_map)):
    for j in char_map[i]:
        text[j] = chr(i)

print("".join(text))

```
