# 🏗️ Calcpad Engineering - Automated Structural Report Generation

Hệ thống tự động hóa tính toán kỹ thuật xây dựng với Calcpad và GitHub Actions.

---

## 📋 Cấu trúc Dự án

```
calcpad_engineering/
├── .github/workflows/main.yml      # GitHub Actions CI/CD
├── cpdinput/                        # Input: Đặt file .cpd ở đây
│   └── parametric_rc_beam.cpd
├── cpdoutput/                       # Output: File .html sinh ra
├── scripts/
│   └── update_index.py             # Script cập nhật danh sách
├── calcpad.html                     # Trang tổng hợp báo cáo
└── Makefile                         # Lệnh tiện ích
```

---

## 🚀 Hướng dẫn Sử dụng

### **1️⃣ Cài đặt cục bộ (Local)**

#### Cài Calcpad CLI:
```bash
dotnet tool install --global Calcpad.Cli --version 7.5.9
```

#### Tạo báo cáo cục bộ:
```bash
# Cách 1: Sử dụng Makefile
make build

# Cách 2: Chạy trực tiếp
calcpad cpdinput/parametric_rc_beam.cpd
```

---

### **2️⃣ Tự động hóa với GitHub Actions**

#### Cách A: Push file .cpd mới
```bash
git add cpdinput/new_report.cpd
git commit -m "Add new structural report"
git push origin main
```
👉 Workflow sẽ **tự động chạy** và sinh file `.html`

#### Cách B: Trigger Workflow hiện tại
```bash
make trigger
```
👉 Hoặc vào GitHub > **Actions** > **Calcpad Automation Workflow** > **Run workflow**

---

### **3️⃣ Xem Báo cáo trực tuyến**

Sau khi Workflow chạy xong (1-2 phút):
1. Kiểm tra tab **Actions** để xem trạng thái
2. Truy cập: https://hydrostructai.github.io/calcpad_engineering/calcpad.html
3. Danh sách báo cáo sẽ tự động cập nhật

---

## 🛠️ Lệnh Makefile

```bash
make test       # Kiểm tra Calcpad đã cài chưa
make build      # Sinh báo cáo cục bộ
make trigger    # Trigger GitHub Action
make clean      # Xóa file HTML
make help       # Xem danh sách lệnh
```

---

## ⚙️ Cấu hình GitHub Pages

1. Vào **Settings** > **Pages**
2. **Source**: `Deploy from a branch`
3. **Branch**: `main`
4. **Folder**: `/ (root)`
5. Nhấn **Save**

---

## 📝 Quy ước Đặt tên File

```
✅ Đúng:     parametric_rc_beam.cpd
❌ Sai:      parametric rc beam.cpd  (có dấu cách)
```

---

## 🔗 Liên kết Hữu ích

- 📊 Báo cáo: https://hydrostructai.github.io/calcpad_engineering/calcpad.html
- 📝 GitHub: https://github.com/hydrostructai/calcpad_engineering
- 🔄 Actions: https://github.com/hydrostructai/calcpad_engineering/actions

---

## ❓ Xử lý Sự cố

### **Workflow chạy thất bại**
1. Vào **Actions** tab > Xem logs chi tiết
2. Thường do:
   - Lỗi cú pháp trong `.cpd`
   - File `.cpd` không được tìm thấy

### **GitHub Pages hiển thị 404**
1. Kiểm tra **Settings > Pages** đã bật chưa
2. Chắc chắn **Branch** là `main`
3. Chờ 1-2 phút để trang cấp nhật

### **File .html không được sinh**
```bash
# Test cục bộ
make build

# Kiểm tra output
ls -lh cpdoutput/
```

---

*Developed for HydrostructAI Engineering Automation Platform*
