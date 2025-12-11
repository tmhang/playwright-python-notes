# Python Automation Course

## Mục tiêu khóa học
Trang bị toàn bộ kiến thức cần thiết để em trở thành **QA Automation Engineer (Playwright Python)** có thể làm dự án thật, apply job remote:
- Python nền tảng + Python cho kiểm thử
- OOP vừa đủ để xây **POM + BasePage** chuẩn
- Playwright Python từ cơ bản → nâng cao → framework
- Pytest (test runner, fixtures, parametrize, markers)
- Git, GitHub & workflow làm việc nhóm
- CI/CD căn bản với GitHub Actions
- API Testing, SQL, Performance (JMeter) mức cần thiết cho Automation

---

## Năng lực đầu ra
Sau khi bám hết giáo trình và làm bài tập nghiêm túc, em sẽ:
- Viết được test UI tự động với Playwright Python theo POM, BasePage
- Thiết kế, tổ chức, refactor framework automation hoàn chỉnh
- Chạy test trên CI (GitHub Actions) với report/video đính kèm
- Viết được test API bằng Python/Playwright
- Dùng SQL để verify dữ liệu
- Dùng JMeter để chạy basic load test
- Làm việc được với Git flow (feature branch, PR, review)

---

## PHASE 1 – Python Fundamentals (≈2 tuần)
**Mục tiêu:** Đủ nền Python để không "đơ" khi đọc/viết code Playwright.

- Cài đặt môi trường:
  - Python 3.x, pip
  - Virtualenv / venv
  - VS Code + extension Python
  - requirements.txt (cài thư viện qua pip)

- Ngày 1–2: Biến, kiểu dữ liệu, toán tử, if/else
  - variable, naming
  - int, float, bool, str
  - toán tử số học, so sánh, logic
  - if / elif / else

- Ngày 3–4: List & Loop
  - list, indexing, slicing
  - for loop
  - break, continue
  - list lồng list (mô phỏng table)

- Ngày 5: Dictionary
  - key / value
  - update, pop, get
  - dict trong list, list trong dict

- Ngày 6: String cho automation
  - lower, upper, strip, replace, split, join
  - xử lý text UI, email, URL

- Ngày 7: Function
  - định nghĩa hàm
  - tham số, giá trị trả về
  - helper function dùng lại

- Ngày 8: Exception & Debug
  - try/except
  - raise
  - tư duy debug (đọc traceback, thêm print/log)

- Ngày 9: File I/O & JSON
  - đọc/ghi file
  - JSON cho API test & config

- Ngày 10: Mini Project Python nhỏ
  - CRUD user / danh sách / filter / validate

---

## PHASE 2 – Python for Test & OOP (≈1–1.5 tuần)
**Mục tiêu:** Hiểu đủ OOP và cấu trúc code để xây POM sau này.

- Control Flow nâng cao
  - for nâng cao, while
  - pattern tìm kiếm, filter list

- OOP Part 1 – Class, Object, Constructor
  - class, object, attribute, method
  - `__init__`, `self`
  - ví dụ class đơn giản theo hướng automation

- OOP Part 2 – Encapsulation & Inheritance
  - đóng gói hành vi
  - BasePage concept
  - class con kế thừa BasePage

- OOP → POM demo nhỏ
  - LoginPage class (giả lập, chưa gắn Playwright)
  - test gọi method của page

---

## PHASE 3 – Pytest Basics (≈1 tuần)
**Mục tiêu:** Nắm test runner chuẩn để chạy Playwright.

- Cài đặt pytest, cấu trúc thư mục tests
- Quy tắc đặt tên file/test
- assert trong pytest
- fixture cơ bản (setup/teardown)
- parametrize (chạy nhiều bộ data)
- markers (skip, smoke, regression …)

---

## PHASE 4 – Playwright Core (≈3 tuần)
**Mục tiêu:** Làm chủ Playwright mức đủ để test mọi web app phổ biến.

- Setup Playwright
  - cài đặt
  - sinh test đầu tiên
  - cấu trúc project base

- Playwright Concepts
  - Browser / Context / Page
  - sync vs async API (chọn 1 hướng ổn định)

- Locator Mastery
  - get_by_text, get_by_role, CSS, XPath
  - nth, filter, locator chaining
  - strict mode & cách fix

- Actions
  - click, fill, type, hover
  - check/uncheck, select
  - upload/download file
  - keyboard, mouse

- Assertions & Waits
  - auto-wait
  - to_be_visible, to_have_text, to_have_url…
  - xử lý flaky test do timing

- Iframe, Popup, Multi-tab
  - switch frame
  - handle new tab/window

- Network & API trong Playwright
  - chặn request/response
  - mock dữ liệu

- LocalStorage, Cookies
  - lưu, đọc, clear

- Tracing, Screenshot, Video
  - bật trace
  - chụp hình, quay video khi fail

---

## PHASE 5 – POM & Framework Architecture (≈2 tuần)
**Mục tiêu:** Từ "biết xài Playwright" → thành "biết xây framework dùng được lâu dài".

- Thiết kế BasePage
  - nhận `page`
  - methods dùng chung (wait, click an toàn…)

- Page Object Model
  - tách locator / action
  - LoginPage, DashboardPage, Menu, v.v.

- Tổ chức thư mục framework
  - `tests/`, `pages/`, `fixtures/`, `config/`, `utils/`, `data/`

- Fixtures nâng cao (pytest + Playwright)
  - tạo browser, context, page dùng lại
  - login trước test (precondition)

- Data-driven tests
  - đọc data từ file (JSON/CSV)
  - chạy test với nhiều bộ data

- Logging & Report
  - tích hợp report HTML
  - log step quan trọng

- Refactor & Best Practices
  - DRY, SRP ở mức QA cần
  - đặt tên rõ nghĩa

---

## PHASE 6 – Git & GitHub (≈1 tuần)
**Mục tiêu:** Làm việc như 1 automation dev trong team.

- Git cơ bản
  - init, clone, add, commit
  - push, pull

- Branching workflow
  - main / develop / feature

- Pull Request & Code Review
- Resolve conflict
- Tagging & versioning

---

## PHASE 7 – CI/CD với GitHub Actions (≈1 tuần)
**Mục tiêu:** Tự động hoá chạy test trên CI.

- Giới thiệu YAML
- Workflow cơ bản
- Setup Python + Playwright trong pipeline
- Run test headless
- Lưu report + video làm artifact
- Thêm badge trạng thái build vào README

---

## PHASE 8 – API Testing (≈1.5 tuần)
**Mục tiêu:** Có khả năng test API ở mức thực dụng cho QA Automation.

- Kiến thức API cơ bản
  - method: GET, POST, PUT, DELETE
  - header, query params, body JSON
  - status code

- Playwright APIRequestContext
  - tạo request context
  - gửi request, đọc response

- Validate response
  - status code
  - field trong JSON

- Data-driven API tests
- Kết hợp API + UI trong cùng suite

---

## PHASE 9 – SQL (≈1 tuần)
**Mục tiêu:** Dùng SQL để verify dữ liệu.

- SELECT cơ bản
- WHERE, ORDER BY, LIMIT
- JOIN (INNER, LEFT)
- GROUP BY, HAVING
- So sánh dữ liệu UI ↔ DB

---

## PHASE 10 – Performance Testing với JMeter (≈1 tuần)
**Mục tiêu:** Hiểu và chạy được basic load test.

- Giới thiệu JMeter UI
- Thread Group, Sampler, Listener
- Config CSV Data
- Assertions
- Các loại test: load, stress, spike (ở mức khái niệm + demo)

---

## PHASE 11 – Final Automation Framework Project (≈2 tuần)
**Mục tiêu:** Có 1 project hoàn chỉnh để show khi xin việc.

- Xây framework full:
  - POM + BasePage + fixtures + config + data
- Viết test suite cho 1 web app demo
- Tích hợp API + UI (nếu phù hợp)
- Chạy trên CI, lưu report & video
- Viết README chuẩn:
  - cách run
  - kiến trúc
  - tech stack

---

## Gợi ý cấu trúc repo
```bash
python-automation-course/
├── README.md
├── day1_basics.md
├── day2_list.md
├── day3_dict.md
├── day4_control_flow.md
├── day5_string.md
├── day6_function.md
├── day7_exception.md
├── day8_oop_class_object.md
├── day9_oop_inheritance_pom.md
├── day10_python_mini_project.md
├── playwright-framework/
│   ├── tests/
│   ├── pages/
│   ├── fixtures/
│   ├── config/
│   ├── data/
│   └── utils/
├── api-tests/
├── sql/
├── performance/
└── final-project/
```

---

## Cách sử dụng giáo trình
1. Mỗi ngày học → tạo file `dayX_*.md` tương ứng, ghi lại lý thuyết + ví dụ + bài tập.
2. Viết code bài tập trong repo riêng (thư mục `practice/` hoặc bên trong từng phần).
3. Khi sang Playwright, bắt đầu build framework song song với học lý thuyết.
4. Cuối khoá, dồn mọi thứ vào `final-project/` để thành 1 sản phẩm có thể show khi xin việc.

Đây là khung chương trình đã được cô đọng để **đủ – đúng – không thừa – không thiếu** cho mục tiêu "zero to hero" với Playwright Python Automation.
