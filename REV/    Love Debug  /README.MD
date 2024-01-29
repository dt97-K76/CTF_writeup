## Challenge Description 
Hello there brave programmer!

I am the CEO of TotallySecureBank™, I have a lot of money in my bank account but I forgot my password! My username is admin and I have $100000 in my account.

If you could recover my account you can use my password as a flag (flag would be uoftctf{MyPasswordHere})

You can try the bank software by running java -jar BankChallenge.jar and use the admin user user with the password

Author: Ido 

File: [BankChallenge.jar](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/BankChallenge.jar)

## Solution

Use [jd-GUI](https://java-decompiler.github.io/) để decompile các file trong tệp `.jar`.
Kết quả: [Main.java](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/Main.java) + [a.java](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/a.java)

Bắt đầu tìm hiểu các câu lệnh tôi chú ý đến đoạn mã sau:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/349affc1-72e2-4071-b9e5-a874a11c52ab)

Sau khi tìm hiêu tôi biết được `Map trong Java được sử dụng để lưu trữ các ánh xạ key-value` có thể đây chính là dữ liệu quan trọng đã được lưu trữ.
Thêm vào đó:
```
String var2 = var0.nextLine(); //user
            if (var1.containsKey(var2){...}
...
String var3 = var0.nextLine(); //pasword
                    if (((a) var1.get(var2)).a(var3)) {...}
```
Như vậy phần nào đã đoán được password sau khi được nhập vào sẽ được mã hóa bởi hàm a(), sau đó được so sánh với dữ liệu được lưu trữ với `map` trước đó.
Để đơn giản tôi sẽ debug để tìm `key-value` và xem chuỗi đã được chương trình mã hóa như thế nào.

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/26ef7759-ff50-4463-8b99-638d99fce10f)

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/f42779da-0314-44ca-9194-d692d32d854e)

Với var3 là password nhập ngẫu nhiên từ bàn phím.

Password admin đúng đã bị encrypt: `瑥⽦䩧㡡倰噕卖䝃捉㉌永敲畴楺癲湊`

Hàm encrypt password trông như sau: 
```
    static String a(String var0) {
        byte[] var1 = var0.getBytes(StandardCharsets.UTF_8);
        int var2 = (int) b[0] ^ 2125394058;

        while (var2 <= var0.length()) {
            int var3 = (int) b[1] ^ 316324253;

            while (var3 < var1.length) {
                var1[var3] = (byte) (var1[var3] + (var2 - ((int) b[2] ^ 322717984)) * var3 + ((int) b[3] ^ 1817181337));
                ++var3;
                a = (int) b[4] ^ 1916880556;
                if ((a * a + a + ((int) b[5] ^ 1376134906)) % ((int) b[6] ^ 1536615318) == 0) {
                }
            }
            ++var2;
        }

        return new String(Base64.getEncoder().encode(var1), StandardCharsets.UTF_16);
    }
```
tương đương với:
```
#encrypt

while i <= len(password):
    j = 0
    while j < len(dec):
        password[j] = ([password][j] + (i - 12) * j + 6) & 0xFF
        j += 1
    i += 1 

Base64.encode(password) -> return as UTF-16 format
```
[Solution](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/solution.py)
```
import base64

password_en = "瑥⽦䩧㡡倰噕卖䝃捉㉌永敲畴楺癲湊"
enc = bytearray(password_en.encode('utf-16be'))
dec = list(base64.b64decode(enc.decode()))
n =1

while n <= len(dec):
    m = 0
    while m < len(dec):
        # Update each byte of the password
        dec[m] = (dec[m] - (n - 12) * m - 6) & 0xFF
        m += 1
    n += 1

print(f"uoftctf{{{''.join([chr(i) for i in dec])}}}")
```

## Challenge Description 
Hello there brave programmer!

I am the CEO of TotallySecureBank™, I have a lot of money in my bank account but I forgot my password! My username is admin and I have $100000 in my account.

If you could recover my account you can use my password as a flag (flag would be uoftctf{MyPasswordHere})

You can try the bank software by running java -jar BankChallenge.jar and use the admin user user with the password

Author: Ido 

File: [BankChallenge.jar](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/BankChallenge.jar)

## Solution

Use [jd-GUI](https://java-decompiler.github.io/) để decompile các file trong tệp `.jar`.
Kết quả: [Main.java](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/Main.java) + [a.java](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/a.java)

Bắt đầu tìm hiểu các câu lệnh tôi chú ý đến đoạn mã sau:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/349affc1-72e2-4071-b9e5-a874a11c52ab)

Sau khi tìm hiêu tôi biết được `Map trong Java được sử dụng để lưu trữ các ánh xạ key-value` có thể đây chính là dữ liệu quan trọng đã được lưu trữ.
Thêm vào đó:
```
String var2 = var0.nextLine(); //user
            if (var1.containsKey(var2){...}
...
String var3 = var0.nextLine(); //pasword
                    if (((a) var1.get(var2)).a(var3)) {...}
```
Như vậy phần nào đã đoán được password sau khi được nhập vào sẽ được mã hóa bởi hàm a(), sau đó được so sánh với dữ liệu được lưu trữ với `map` trước đó.
Để đơn giản tôi sẽ debug để tìm `key-value` và xem chuỗi đã được chương trình mã hóa như thế nào.

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/26ef7759-ff50-4463-8b99-638d99fce10f)

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/f42779da-0314-44ca-9194-d692d32d854e)

Với var3 là password nhập ngẫu nhiên từ bàn phím.

Password admin đúng đã bị encrypt: `瑥⽦䩧㡡倰噕卖䝃捉㉌永敲畴楺癲湊`

Hàm encrypt password trông như sau: 
```
    static String a(String var0) {
        byte[] var1 = var0.getBytes(StandardCharsets.UTF_8);
        int var2 = (int) b[0] ^ 2125394058;

        while (var2 <= var0.length()) {
            int var3 = (int) b[1] ^ 316324253;

            while (var3 < var1.length) {
                var1[var3] = (byte) (var1[var3] + (var2 - ((int) b[2] ^ 322717984)) * var3 + ((int) b[3] ^ 1817181337));
                ++var3;
                a = (int) b[4] ^ 1916880556;
                if ((a * a + a + ((int) b[5] ^ 1376134906)) % ((int) b[6] ^ 1536615318) == 0) {
                }
            }
            ++var2;
        }

        return new String(Base64.getEncoder().encode(var1), StandardCharsets.UTF_16);
    }
```
tương đương với:
```
#encrypt

while i <= len(password):
    j = 0
    while j < len(dec):
        password[j] = ([password][j] + (i - 12) * j + 6) & 0xFF
        j += 1
    i += 1 

Base64.encode(password) -> return as UTF-16 format
```
[Solution](https://github.com/datvn09/CTF_writeup/edit/main/REV/%20%20%20%20CEO's%20Lost%20Password/solution.py)
```
import base64

password_en = "瑥⽦䩧㡡倰噕卖䝃捉㉌永敲畴楺癲湊"
enc = bytearray(password_en.encode('utf-16be'))
dec = list(base64.b64decode(enc.decode()))
n =1

while n <= len(dec):
    m = 0
    while m < len(dec):
        # Update each byte of the password
        dec[m] = (dec[m] - (n - 12) * m - 6) & 0xFF
        m += 1
    n += 1

print(f"uoftctf{{{''.join([chr(i) for i in dec])}}}")
```
















