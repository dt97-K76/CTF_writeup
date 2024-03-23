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
Giá trị này được lưu lần lượt vào map[char_input].

Phân tích hàm `erialize_and_output`:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/526c4381-1132-4d25-a2b4-d2f1986c6e76)


index chạy từ 1->254 gán v2 = map[index] ghi vào output chiều dài của v2 (tức số lần xuất hiện của index) và các giá trị của mảng v2 ( tức vị trí xuất hiện của index).

solution:

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

kết qủa:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/b6649aff-da38-419c-a568-7fd2e8ae8bfa)

flag: `HTB{4_v3ry_b4d_compr3ss1on_sch3m3}`

