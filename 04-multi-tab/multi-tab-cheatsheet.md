# MULTI-TAB CHEAT SHEET – PLAYWRIGHT PYTHON

Dùng để dạy + làm việc thật, không phải ghi chú chơi.

---

## 1. Tư duy gốc – Cấu trúc Browser / Context / Page

| Khái niệm         | Giải thích ngắn                                                    | Code / Ghi chú                              |
| ----------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| `browser`         | Ứng dụng browser thật (Chromium/WebKit/Firefox)                  | Khởi tạo từ `playwright.chromium.launch()` |
| `BrowserContext`  | 1 “profile” trong browser. Mỗi context là 1 phiên làm việc riêng | `context = browser.new_context()`          |
| `Page`            | Mỗi tab/window trong 1 context                                    | `page = context.new_page()`                |
| Multi-tab         | Làm việc với **nhiều Page** trong **cùng 1 context**             | Dùng `context.pages`                        |
| Tạo tab           | Tạo tab mới trong cùng context                                    | `page2 = context.new_page()`               |
| Lấy danh sách tab | Lấy tất cả Page hiện có trong context                             | `pages = context.pages`                    |

Ví dụ:

```python
context = browser.new_context()
page = context.new_page()      # tab 1
page2 = context.new_page()     # tab 2
pages = context.pages          # list tất cả tab trong context
2. API quan trọng – Cần thuộc
| API                          | Thuộc đối tượng  | Khi dùng                                      | Ghi chú nhanh                      |
| ---------------------------- | ---------------- | --------------------------------------------- | ---------------------------------- |
| `context.pages`              | `BrowserContext` | Lấy danh sách tất cả tab (Page) đang mở       | Trả về `list[Page]`                |
| `context.new_page()`         | `BrowserContext` | Tự tạo thêm tab mới trong cùng context        | Không dùng `expect_popup` case này |
| `page.expect_popup()`        | `Page`           | Khi **chính page này** click → mở tab mới     | Dùng khi biết rõ click nào mở tab  |
| `context.expect_page()`      | `BrowserContext` | Khi tab mới mở nhưng không rõ bắn từ page nào | Ít phụ thuộc `page` cụ thể         |
| `page.bring_to_front()`      | `Page`           | Đưa tab đó lên foreground (switch tab)        | Dùng khi cần “focus” vào 1 tab     |
| `page.close()`               | `Page`           | Đóng tab hiện tại                             | Hay dùng dọn dẹp tab thừa          |
| `page.url`                   | `Page`           | Lấy URL hiện tại của tab                      | Dùng để assert điều hướng          |
| `page.title()`               | `Page`           | Lấy title của tab                             | Dùng để assert tiêu đề             |
| `page.wait_for_load_state()` | `Page`           | Đợi tab load xong trước khi thao tác / assert | Tránh flaky test với tab mới       |
3. Pattern 1 – Click link target="_blank" mở tab mới
3.1. Chuẩn nhất: dùng page.expect_popup()

Dùng khi page hiện tại click link và mở tab mới.
from playwright.sync_api import expect

with page.expect_popup() as popup_info:
    page.locator("text=Click Here").click()   # link có target="_blank"

new_page = popup_info.value
new_page.wait_for_load_state()

assert "/windows/new" in new_page.url
expect(new_page.locator("h3")).to_have_text("New Window")

Quy tắc:

Khối with page.expect_popup() phải bọc đúng hành động gây mở tab.

Click nhầm element không mở tab mới → timeout “waiting for event popup”.
3.2. Khi nghi ngờ → dùng context.expect_page()

Dùng khi:

Không chắc tab mới bắn từ page nào, hoặc

JS mở tab bằng cách “lạ”.
with page.context.expect_page() as page_info:
    page.locator("text=Click Here").click()

new_page = page_info.value
new_page.wait_for_load_state()
4. Pattern 2 – Quản lý nhiều tab đã mở
4.1. Lấy toàn bộ tab
pages = context.pages
for p in pages:
    print(p.url)

4.2. Switch tab
dashboard_page = context.pages[0]
settings_page  = context.pages[1]

settings_page.bring_to_front()
# ... assert ở Settings ...

dashboard_page.bring_to_front()
# ... tiếp tục thao tác trên Dashboard ...


Nên đặt tên biến rõ ràng: login_page, dashboard_page, settings_page, …

4.3. Đóng các tab thừa, giữ 1 tab
for p in context.pages[1:]:  # giữ tab đầu
    p.close()

5. Pattern 3 – Tự tạo tab mới bằng code

Không có click, tự mở tab:

new_page = context.new_page()
new_page.goto("https://google.com")
new_page.bring_to_front()


Case này không dùng expect_popup.

6. Pattern 4 – Đếm tab trước/sau click (cách “thủ công”)

Dùng khi không muốn/không thể dùng expect_* nhưng vẫn cần đảm bảo có tab mới.

old_count = len(context.pages)

page.locator("text=Click Here").click()

for _ in range(10):  # tối đa ~5s
    if len(context.pages) > old_count:
        break
    page.wait_for_timeout(500)

assert len(context.pages) == old_count + 1
new_page = context.pages[-1]
new_page.wait_for_load_state()

7. Các lỗi kinh điển cần tránh
| Lỗi / Triệu chứng                     | Nguyên nhân gốc                                                                          | Cách fix cụ thể                                                                                                   |
| ------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Timeout “waiting for event popup”     | Click nhầm element; element không mở tab mới; không có `target="_blank"` / `window.open` | Inspect HTML: kiểm tra đúng link; dùng locator chuẩn `text=…`, `a[href='/path']`.                                 |
| Nhầm “tab UI” với “browser tab”       | Tab trong UI (Overview/Details) thực ra vẫn cùng 1 Page                                  | Đây **không phải** multi-tab browser → click + assert bình thường, **không dùng** `expect_popup` / `expect_page`. |
| Mất reference tab gốc                 | Không lưu `login_page = page` trước khi mở thêm tab                                      | Luôn lưu biến: `login_page`, `profile_page`, `settings_page`… để dùng lại.                                        |
| Không `wait_for_load_state()` tab mới | Assert quá sớm, trang chưa load xong → test fail ngẫu nhiên                              | Sau khi có `new_page`, luôn gọi `new_page.wait_for_load_state()` trước khi thao tác.                              |
| Dùng nhầm API                         | Chỉ chuyển route trong cùng tab nhưng lại dùng `expect_popup`                            | Chỉ khi có **tab mới** → dùng `expect_popup` / `context.expect_page`. Điều hướng trong cùng tab → click thường.   |
8. Mini checklist khi gặp multi-tab
| Câu hỏi kiểm tra                                    | Trả lời                                 | Hành động đúng                                                                                                      |
| --------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Link này có thực sự mở tab mới không?               | Có `target="_blank"` hoặc `window.open` | Bọc click trong `with page.expect_popup()` hoặc `with context.expect_page()`.                                       |
|                                                     | Không                                   | Chỉ là điều hướng trong cùng tab → click thường + assert, **không** dùng multi-tab API.                             |
| Đã lưu Page gốc chưa?                               | Chưa                                    | Ngay sau login: `main_page = page` hoặc `login_page = page`.                                                        |
| Click mở tab mới đã bọc trong `expect_*` chưa?      | Chưa                                    | `python\nwith main_page.expect_popup() as p_info:\n    main_page.locator("...").click()\nnew_page = p_info.value\n` |
| Sau khi mở tab mới đã `wait_for_load_state()` chưa? | Chưa                                    | `new_page.wait_for_load_state()` trước khi assert URL/heading.                                                      |
| Cần switch qua lại giữa các tab không?              | Có                                      | `new_page.bring_to_front()` rồi xong việc thì `main_page.bring_to_front()`.                                         |
| Cần dọn dẹp tab thừa không?                         | Có                                      | `python\nfor p in context.pages[1:]:\n    p.close()\n` giữ lại tab chính.                                           |

