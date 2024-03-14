# Challenge RE

## packer
## FactCheck
## WinAntiDbg0x100
## WinAntiDbg0x200
## WinAntiDbg0x300
## Classic Crackme 0x100

```
secret1 = 85
secret2 = 51
secret3 = 15
fix = 97

def encode_text(input1, secret1, secret2, secret3, fix, i_0):
    for t in range(65, 125):
        input_val = t
        for i in range(3):
            random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
            random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
            x = ((random2 & secret3) + input_val - fix + (secret3 & (random2 >> 4))) 
            if x < 0:
                input_val = x + fix
            else:
                input_val = x % 26 + fix
        if input_val == input1:
            print(chr(t), end="")
            break

output = "mpknnphjngbhgzydttvkahppevhkmpwgdzxsykkokriepfnrdm"

for i_0 in range(len(output)):
    encode_text(ord(output[i_0]), 85, 51, 15, 97, i_0)

# mmhhkjbaka\_aqpXqnpb[_gd_m__ddkXatrjsbbcei`YgZbc^d

```

## weirdSnake

```
# Define input list
input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 106, 123, 89, 87, 18, 62, 47, 10, 78]

key_str = 't_Jo3'

key_list = [ord(char) for char in key_str]

while len(key_list) < len(input_list):
    key_list.extend(key_list)

#print(key_list)

result = [a ^ b for a, b in zip(input_list, key_list)]

# Convert ASCII codes back to characters and join them into a string
result_text = ''.join(map(chr, result))

print(result_text)

#picoCTF{N0t_sO_coNfus1ng_sn@ke_516dfaee}
```
