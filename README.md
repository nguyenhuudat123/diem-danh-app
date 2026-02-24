# Daily Work Status Generator (App Điểm Danh Thông Minh)

Đây là một ứng dụng desktop đơn giản được viết bằng Python (sử dụng thư viện `tkinter`). Ứng dụng giúp tự động tạo và sao chép các mẫu tin nhắn báo cáo bắt đầu và kết thúc công việc bằng tiếng Hàn, đi kèm với ngày tháng hiện tại. 

Dự án này phù hợp cho những người làm việc trong môi trường công ty Hàn Quốc hoặc có yêu cầu báo cáo trạng thái làm việc hàng ngày trên các nền tảng nhắn tin như KakaoTalk, Slack, Zalo, Telegram...

## Tính năng chính

* **Giao diện đồ họa (GUI) trực quan:** Thiết kế đơn giản với các nút bấm lớn, dễ thao tác.
* **Lưu trữ dữ liệu người dùng:** Tự động lưu tên người dùng vào file văn bản cục bộ (`user_settings.txt`). Tên này sẽ được tự động tải lên trong các lần mở ứng dụng tiếp theo.
* **Tự động tạo thời gian:** Lấy ngày tháng hiện tại của hệ thống và định dạng theo chuẩn `YY.MM.DD`.
* **Tự động sao chép (Auto-copy to Clipboard):** Khi nhấn nút tạo tin nhắn, nội dung sẽ được tự động lưu vào bộ nhớ tạm (Clipboard), người dùng chỉ cần nhấn `Ctrl + V` để dán vào khung chat mà không cần bôi đen copy thủ công.
* **Định dạng tin nhắn có sẵn:** * **START:** `[YY.MM.DD] - [Tên người dùng] 업무 시작하겠습니다~` (Bắt đầu công việc)
    * **END:** `[YY.MM.DD] - [Tên người dùng] 업무 마치겠습니다~` (Kết thúc công việc)

## Yêu cầu hệ thống

* Ngôn ngữ: **Python 3.x**
* Thư viện: `tkinter` (Đây là thư viện tiêu chuẩn của Python, thường đã được cài đặt sẵn cùng với Python trên Windows/macOS).

## Hướng dẫn cài đặt và sử dụng

### 1. Chạy trực tiếp bằng Python
**Bước 1:** Clone repository này về máy của bạn:
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
