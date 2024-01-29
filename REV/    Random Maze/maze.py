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



        


