**1. Cấu hình Git lần đầu trên máy**:

git config --global user.name "TenCuaEm"

git config --global user.email "email@example.com"

# Windows: tránh lỗi xuống dòng

git config --global core.autocrlf true

# Linux/Mac:

# git config --global core.autocrlf input

git config --list   # xem lại config

**2. Bắt đầu với repo**

**2.1. Clone repo về máy**

git clone https://github.com/USERNAME/PlaywrightPython.git
cd PlaywrightPython

**2.2. Khởi tạo repo mới từ folder sẵn có**

cd HangTM_POM

git init

git remote add origin https://github.com/USERNAME/PlaywrightPython.git

git add .

git commit -m "Initial commit"

git push -u origin main

**3. Flow chuẩn cho MỖI TASK (bài tập / feature):**

**#1. Cập nhật main mới nhất:**

git checkout main

git pull origin main

**#2. Tạo branch mới cho task:**

    git checkout -b feature/b9-multitab
    
**#3 Code + chạy test local.**

**#4 Add + commit:**


git status

git add .

git commit -m "Add tests for bai 9: multi tab"

Push branch lên remote:

git push -u origin feature/b9-multitab


Lên GitHub → tạo Pull Request:

base: main ← compare: feature/b9-multitab → review → merge.

Sau khi merge xong:

git checkout main

git pull origin main

git branch -d feature/b9-multitab          # xóa branch local (nếu muốn)

git push origin --delete feature/b9-multitab  # xóa branch trên remote (nếu muốn)

**. Các lệnh Git dùng hàng ngày**

**4.1. Kiểm tra trạng thái + diff**

git status          # xem file mới / sửa / đang staged

git diff            # xem diff file chưa add

git diff --staged   # diff file đã git add


**4.2. Thêm file + commit**

git add .                               # add tất cả

# hoặc
git add tests/test_login.py

git add pages/login_page.py

git commit -m "Mo ta ro rang, ngan gon"

**4.3. Làm việc với branch**

git branch                # liệt kê branch local

git branch -vv            # thêm info tracking

git checkout main         # chuyển branch

git checkout HangTM_POM

git checkout -b feature/b9      # tạo branch mới từ branch hiện tại

git branch -d feature/b9        # xóa branch local

**5. Làm việc với remote (origin)**

git remote -v                                      # xem remote

git remote add origin https://github.com/....git   # thêm remote

git pull origin main                               # kéo code từ remote

git pull origin HangTM_POM

git push -u origin feature/b9                      # push lần đầu

git push                                           # những lần sau

**6. Cập nhật branch feature từ main**

Khi main đã được update (merge PR khác) và em muốn kéo về branch mình:

git checkout main

git pull origin main          # main mới nhất

git checkout feature/b9

git merge main                # merge main vào feature/b9

# nếu có conflict → fix → git add → git commit

(Chỉ dùng rebase khi đã hiểu rõ, tránh loạn.)

**7. Lưu tạm việc đang dở (stash)**

Đang code dở mà phải chuyển sang branch khác:

git status

git stash             # cất tạm toàn bộ thay đổi chưa commit

git checkout main


Quay lại làm tiếp:

git checkout feature/b9

git stash list        # xem các stash

git stash apply       # apply lại stash mới nhất

**8. Xem lịch sử và tìm commit**

git log --oneline

git log --oneline --graph --all       # nhìn tổng quan

git log --oneline -- tests/test_login.py   # lịch sử 1 file

**9. Undo những bước sai (các mức độ)**

Bỏ stage (undo git add):

git reset HEAD tests/test_login.py


Hủy thay đổi ở file (quay lại như commit gần nhất):

git checkout -- tests/test_login.py


Quay lại commit trước (mạnh, xóa luôn commit mới):

git reset --hard HEAD~1


Chỉ dùng reset --hard khi chắc chắn vì sẽ mất thay đổi chưa push.

**10. Các lỗi GIT mà em hay gặp và cách đọc nhanh**

error: src refspec <branch> does not match any

→ Branch <branch> không tồn tại local hoặc chưa có commit nào.

→ Kiểm tra bằng git branch, nếu cần thì git checkout -b <branch> và commit trước khi push.

fatal: The current branch <branch> has no upstream branch

→ Chưa gắn branch local với remote.

→ Dùng:

git push -u origin <branch>


fatal: 'orgin' does not appear to be a git repository

→ Gõ sai origin. Không có remote tên đó.

error: GH013: Repository rule violations... Changes must be made through a pull request.

→ Repo cấm push trực tiếp lên main.

→ Phải push lên branch khác (feature/...) rồi tạo Pull Request.

