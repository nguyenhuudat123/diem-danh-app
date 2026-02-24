import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

# Tên file để lưu cấu hình
CONFIG_FILE = "user_settings.txt"

def load_name():
    """Hàm đọc tên từ file, nếu không có thì trả về 'Dat'"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            saved_name = f.read().strip()
            return saved_name if saved_name else "Dat"
    return "Dat"

def save_name(name):
    """Hàm lưu tên vào file"""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(name)

def update_and_copy(status_type):
    # Lấy tên hiện tại từ ô nhập tên và lưu lại vào file
    current_name = entry_name.get().strip()
    if not current_name:
        messagebox.showwarning("Chú ý", "Bạn chưa nhập tên kìa!")
        return
        
    save_name(current_name) # Lưu lại để lần sau mở app vẫn thấy tên này
    
    # Lấy ngày hiện tại
    date_str = datetime.now().strftime("%y.%m.%d")
    
    # Xác định nội dung
    if status_type == "START":
        content = f"{date_str} - {current_name} 업무 시작하겠습니다~"
    else:
        content = f"{date_str} - {current_name} 업무 마치겠습니다~"
    
    # Hiển thị lên ô kết quả
    entry_result.delete(0, tk.END)
    entry_result.insert(0, content)
    
    # Tự động copy vào Clipboard
    root.clipboard_clear()
    root.clipboard_append(content)
    
    label_notice.config(text=f"✔ Đã lưu tên '{current_name}' và copy vào Clipboard!")

# Khởi tạo màn hình chính
root = tk.Tk()
root.title("App Điểm Danh Thông Minh")
root.geometry("400x650")
root.configure(bg="#FFF9C4")

# --- Khu vực nhập tên ---
label_name_tag = tk.Label(root, text="Tên của bạn:", font=("Arial", 10, "bold"), bg="#FFF9C4")
label_name_tag.pack(pady=(20, 0))

entry_name = tk.Entry(root, font=("Arial", 12), width=20, justify='center')
entry_name.insert(0, load_name()) # Load tên đã lưu hoặc "Dat" khi mở app
entry_name.pack(pady=5)

# Tiêu đề app
label_title = tk.Label(root, text="ĐIỂM DANH", font=("Arial", 18, "bold"), bg="#FFF9C4", fg="#5D4037")
label_title.pack(pady=30)

# Ô hiển thị kết quả để copy
entry_result = tk.Entry(root, font=("Arial", 11), width=35, justify='center', bd=2)
entry_result.pack(pady=10)

# Dòng thông báo trạng thái
label_notice = tk.Label(root, text="Nhập tên và nhấn nút bên dưới", font=("Arial", 9, "italic"), bg="#FFF9C4", fg="#2E7D32")
label_notice.pack(pady=10)

# Khung chứa 2 nút
frame_buttons = tk.Frame(root, bg="#FFF9C4")
frame_buttons.pack(expand=True)

btn_start = tk.Button(frame_buttons, text="START", 
                      command=lambda: update_and_copy("START"), 
                      bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), 
                      width=15, height=3)
btn_start.pack(pady=15)

btn_end = tk.Button(frame_buttons, text="END", 
                    command=lambda: update_and_copy("END"), 
                    bg="#F44336", fg="white", font=("Arial", 12, "bold"), 
                    width=15, height=3)
btn_end.pack(pady=15)

root.mainloop()