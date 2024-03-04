Challenge đơn giản tìm các kí tự mã ascii tương ứng theo thứ tự (bảng chữ cái là các ẩn). Sử dụng Z3 để solve

```
from z3 import *

# Khởi tạo solver
solver = Solver()

# Khai báo biến
variables = {}
for char in 'abcdefghijklmnopqrstuvwxyz':
    variables[char] = Int(char)

# Thêm các ràng buộc vào solver
solver.add(
    variables['b'] + variables['c'] + variables['w'] == 314,
    variables['t'] + variables['d'] + variables['u'] == 290,
    variables['p'] + variables['w'] + variables['e'] == 251,
    variables['v'] + variables['l'] + variables['j'] == 274,
    variables['a'] + variables['t'] + variables['b'] == 344,
    variables['b'] + variables['j'] + variables['m'] == 255,
    variables['h'] + variables['o'] + variables['u'] == 253,
    variables['q'] + variables['l'] + variables['o'] == 316,
    variables['a'] + variables['g'] + variables['j'] == 252,
    variables['q'] + variables['x'] + variables['q'] == 315,
    variables['t'] + variables['n'] + variables['m'] == 302,
    variables['d'] + variables['b'] + variables['g'] == 328,
    variables['e'] + variables['o'] + variables['m'] == 246,
    variables['v'] + variables['v'] + variables['u'] == 271,
    variables['f'] + variables['o'] + variables['q'] == 318,
    variables['s'] + variables['o'] + variables['j'] == 212,
    variables['j'] + variables['j'] + variables['n'] == 197,
    variables['s'] + variables['u'] + variables['l'] == 213,
    variables['q'] + variables['w'] + variables['j'] == 228,
    variables['i'] + variables['d'] + variables['r'] == 350,
    variables['e'] + variables['k'] + variables['u'] == 177,
    variables['w'] + variables['n'] + variables['a'] == 288,
    variables['r'] + variables['e'] + variables['u'] == 212,
    variables['q'] + variables['l'] + variables['f'] == 321
)

# Kiểm tra và lấy giá trị của biến
if solver.check() == sat:
    model = solver.model()
    result = {char: model[variables[char]].as_long() for char in variables if model[variables[char]] is not None}
    print(result)
    result_string = ''.join(chr(result[char]) for char in sorted(result))
    print(result_string)
else:
    print("No solution found.")
#osu{0rZ_p3PpY_my_s4v1oR}
```
