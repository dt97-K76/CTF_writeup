# Warmup

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/3ead1770-99b6-4979-a104-5b6664ef3301)

Mở IDA xem mã nguồn:
![image](https://github.com/datvn09/CTF_writeup/assets/157048397/17f82a16-e2fb-4a51-8fa8-5e91fc486841)

Mã nguồn khá đơn giản và mình chỉ cần quan tâm đoạn này, tức chuỗi flag khi nhập vào được biến dổi tại hàm sub_401080 và so sánh với unk_403188 (21 kí tự)

Xem xét hàm sub_401080:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/19c60cb8-5a14-4965-bd6f-2baf97cb746f)

tôi sẽ debug để lấy giá trị của biến result

# Solution 
```
unk_E93188 = [0x3C,0x41,0x9D,0x32,0x87,0x4A,0xD5,0x2B,0x52,0x56,0xB6,0xE6,0x74,0xBA,0xAA,0x05,0x7E,0x1A,0x04,0x19,0x13,0x00,0x00,0x00]

flag =''
enc = [0x77,0xc,0xdc,0x71,0xd3,0xc,0xae,0x59,0x31,0x62,0xe9,0x88,0x11,0xec,0x99,0x77,0x21,0x7e,0x35,0x5c,0x6e,0xd4,0x28]

for i in range (21):
    flag+=chr(unk_E93188[i]^enc[i])
    
print(flag)
#KMACTF{rc4_neV3r_d1E}
```

![Uploading image.png…]()






