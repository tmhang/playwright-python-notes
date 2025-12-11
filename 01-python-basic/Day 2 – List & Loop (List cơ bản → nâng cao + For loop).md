# Day 2 – List & Loop (List cơ bản → nâng cao + For loop)

Day 2 rất quan trọng vì cả UI automation và API testing đều dùng list & loop liên tục. Em phải nắm cực chắc phần này.

---

# 1. List là gì?

List = tập hợp nhiều giá trị trong **một biến**.

```python
roles = ["admin", "manager", "staff"]
```

Đặc điểm:

* Có thứ tự (index)
* Thay đổi được
* Có thể chứa mọi kiểu dữ liệu (kể cả list bên trong list)

---

# 2. Truy cập phần tử bằng index

```python
roles[0]      # phần tử đầu
roles[1]      # phần tử thứ 2
roles[-1]     # phần tử cuối
```

---

# 3. Các hàm quan trọng của List (bắt buộc thuộc)

## 3.1. `len()` – chiều dài list

```python
len(roles)
```

## 3.2. Thêm phần tử

```python
roles.append("guest")
roles.insert(1, "hr")
```

## 3.3. Xoá phần tử

```python
roles.remove("staff")
roles.pop(1)          # xoá theo index
```

## 3.4. Kiểm tra tồn tại

```python
if "admin" in roles:
    print("Tồn tại")
```

---

# 4. LOOP – For loop

Dùng để duyệt qua list, rất thường gặp trong automation.

## 4.1. Cú pháp

```python
for item in list:
    print(item)
```

Ví dụ:

```python
for r in roles:
    print("Role:", r)
```

---

# 5. List nâng cao – List lồng List (giống bảng dữ liệu UI)

Dạng này cực kỳ phổ biến khi duyệt table.

```python
users = [
    ["Hang", "admin"],
    ["Lan", "manager"],
    ["An", "hr"]
]
```

## Duyệt từng user

```python
for u in users:
    print("Tên user:", u[0], "- role:", u[1])
```

---

# 6. Loop nâng cao – duyệt theo index

Khi cần biết vị trí phần tử.

```python
for i in range(len(roles)):
    print(i, roles[i])
```

---

# 7. Thực hành Day 2

## Bài 1 – Tạo list role và in:

* tổng số role
* role đầu tiên
* role cuối cùng

## Bài 2 – Thêm mới & xoá role

* thêm `hr`, `guest`
* xoá `manager`

## Bài 3 – Kiểm tra role tồn tại

Kiểm tra "admin" có trong list không.

## Bài 4 – Duyệt list user (list lồng list)

In ra:

```
Tên user: Hang – role: admin
Tên user: Lan – role: manager
Tên user: An – role: hr
```

## Bài 5 – Nâng cao

Tìm tất cả user có role = "admin" và in ra.

---

# 8. Cheat Sheet Day 2 (học thuộc)

```
len(list)
list.append(x)
list.insert(i, x)
list.remove(x)
list.pop(i)
x in list
for item in list:
for i in range(len(list)):
```

---

# 9. Checklist Day 2

* [ ] Hiểu list và index
* [ ] Dùng được append / insert / remove / pop
* [ ] Kiểm tra được phần tử trong list với `in`
* [ ] Viết được for loop duyệt list
* [ ] Hiểu list lồng list & cách lấy dữ liệu
* [ ] Hoàn thành cả 5 bài tập

Khi tick hết checklist → sẵn sàng sang **Day 3 – Dictionary & Loop nâng cao**.
