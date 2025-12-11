# Day 1 – Python Basics (Biến, Kiểu dữ liệu, Toán tử, If/Else)

Day 1 đặt nền tảng để em không bị "đơ" khi bắt đầu viết code Playwright. Toàn bộ bài học phải thật chắc.

---

# 1. Biến (Variables)

Biến dùng để lưu trữ dữ liệu.

## Quy tắc:

* Chỉ dùng chữ cái, số, underscore
* Không bắt đầu bằng số
* Không có dấu cách

```python
name = "Hang"
age = 42
is_admin = True
```

---

# 2. Kiểu dữ liệu (Data Types)

Các kiểu quan trọng cho Automation:

## 2.1. `int` – số nguyên

```python
age = 42
```

## 2.2. `float` – số thập phân

```python
price = 10.5
```

## 2.3. `str` – chuỗi

```python
username = "admin"
```

## 2.4. `bool` – đúng/sai

```python
is_active = True
```

## 2.5. `None` – không có giá trị

```python
result = None
```

---

# 3. Toán tử (Operators)

## 3.1 Toán tử số học

```python
+, -, *, /, //, %, **
```

Ví dụ:

```python
x = 10
y = 3
print(x // y)  # chia lấy nguyên
```

## 3.2 Toán tử so sánh

```python
==, !=, >, <, >=, <=
```

## 3.3 Toán tử logic

```python
and, or, not
```

---

# 4. If – Elif – Else (Cấu trúc điều kiện)

Dùng để quyết định logic.

## 4.1 Cú pháp

```python
if condition:
    # do something
elif condition2:
    # do something
else:
    # do something
```

## 4.2 Ví dụ thực tế (Automation mindset)

```python
status_code = 200

if status_code == 200:
    print("Request OK")
elif status_code == 404:
    print("Not Found")
else:
    print("Unexpected error")
```

---

# 5. Ép kiểu (Type casting)

```python
x = int("10")
y = str(123)
z = float("3.14")
```

---

# 6. Input (giả lập người dùng nhập)

Dùng cho một số bài tập.

```python
name = input("Nhập tên: ")
print("Hello", name)
```

---

# 7. Thực hành Day 1

## Bài 1: Tạo 3 biến và in ra kiểu dữ liệu

```python
username = "Hang"
age = 42
is_admin = False

print(type(username))
print(type(age))
print(type(is_admin))
```

## Bài 2: Kiểm tra điểm đậu/rớt

```python
score = 75
if score >= 50:
    print("Đậu")
else:
    print("Rớt")
```

## Bài 3: Kiểm tra role người dùng

```python
role = "admin"

if role == "admin":
    print("Có toàn quyền")
elif role == "manager":
    print("Quản lý")
else:
    print("Người dùng thường")
```

---

# 8. Checklist Day 1

* [ ] Hiểu biến, kiểu dữ liệu
* [ ] Phân biệt int / float / str / bool
* [ ] Nắm toán tử so sánh & logic
* [ ] Viết được if/elif/else
* [ ] Làm xong cả 3 bài tập

Khi hiểu hết Day 1, em sẵn sàng sang **Day 2 – List & Loop**.
