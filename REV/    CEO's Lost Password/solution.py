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