# Baby

https://web-osu-wysi.surge.sh/

Mã code của chương trình như sau:
```

    var combos = [];

    function wysi() {
      if (combos.length === 8) {
        var cs = combos.join("");
        var csr = cs + cs.split("").reverse().join("");
        var res = CryptoJS.AES.decrypt("5LJJj+x+/cGxhxBTdj/Q2RxkhgbH7v8b/IgX9Kjptpo=", CryptoJS.enc.Hex.parse(csr + csr), { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8);
        // if prefix is "osu{" then its correct
        if (res.startsWith("osu{")) {
          document.getElementById("music").innerHTML = '<audio src="./wysi.mp3" autoplay></audio>';
          console.log(res);
        } else {
          // reset
          console.log("nope.");
          combos = [];
        }
      }
    }

    $(document).ready(function() {
      $("#frame").on("click", "button", function() {
        var buttonValue = $(this).data("value");
        combos.push(buttonValue);
        wysi();
      });
    });
  ```

Như vậy dễ thấy chỉ cần decrypt chuỗi `5LJJj+x+/cGxhxBTdj/Q2RxkhgbH7v8b/IgX9Kjptpo=` được mã hóa bởi AES mod ECB với key được tạo từ 8 kí tự dựa vào data của đoạn mã. Tìm data:

![image](https://github.com/datvn09/CTF_writeup/assets/157048397/02a9999e-3173-4f79-a220-a8bd82af35bd)

xem source kết luận vậy data_value là các số từ 0->9 

solution:

```
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

for i in range(10000000, 100000000):
    cs = str(i)
    csr = cs + cs[::-1]
    csr = csr + csr
    key = bytes.fromhex(csr) 
    print (key)
    enc = b'5LJJj+x+/cGxhxBTdj/Q2RxkhgbH7v8b/IgX9Kjptpo='
    enc = b64decode(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    dec = cipher.decrypt(enc)
    if b'osu{' in dec:
        print(dec)
        break


```



