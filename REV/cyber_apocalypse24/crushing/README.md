## Describe
```
You managed to intercept a message between two event organizers. Unfortunately, it's been compressed with their proprietary message transfer format. Luckily, they're gamemakers first and programmers second - can you break their encoding?

Author: clubby789
```

## Solution 

Đối với challenge này, tôi nhận được hai tệp. Một tệp nhị phân và một tệp có tên message.txt.cz chứa dữ liệu được mã hóa.

Mở tệp nhị phân với IDA và bắt đầu phân tích:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/cd9b5a1c-6a67-4588-94d9-820f833e5f18)

Ngắn gọn, dễ hiểu chương trình nhận từng kí tự đầu vào và xử lí kí tự đó tại hàm 
`add_char_to_map` cuối cùng đầu ra output tại hàm `serialize_and_output`

Phân tích hàm `add_char_to_map`:

Sau khi rename lại các biến ta được đoạn code dễ hiểu hơn:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/f008759e-1454-4895-b4f2-391c2c7b4b6c)

Giá trị trả về của hàm là `result` tức giá trị biến i truyền vào nó là thứ tự của `char_input`

Giá trị của biến i truyền vào này sẽ được 








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
