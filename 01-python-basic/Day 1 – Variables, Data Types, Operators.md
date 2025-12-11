## 1. Biến (Variable)
name = "Hang"
age = 42
is_active = True


Quy tắc:

không bắt đầu bằng số

không chứa dấu cách

nên dùng chữ thường + _

## 2. Kiểu dữ liệu cơ bản

| Kiểu    | Ví dụ              |
| ------- | ------------------ |
| `str`   | `"hello"`          |
| `int`   | `25`               |
| `float` | `3.14`             |
| `bool`  | `True`, `False`    |
| `list`  | `["a", "b", "c"]`  |
| `dict`  | `{"name": "Hang"}` |
## 3. Hàm hay dùng

▶ print()
print("Hello", name)

▶ len() – đếm số ký tự / phần tử
len("hello")     # 5
len([1,2,3])     # 3

## 4. Toán tử trong Python
Toán học
+, -, *, /, //, %, **

So sánh
==, !=, >, <, >=, <=

Logic
and, or, not

## 5. If – Else
age = 20

if age >= 18:
    print("Đủ tuổi")
else:
    print("Chưa đủ tuổi")
