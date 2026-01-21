# GitHub Actions Calcpad Automation

## 🚀 Quy Trình Tự Động

### Trigger
- **Điều kiện**: Push file `.cpd` vào folder `cpdinput/`
- **Event**: `on: push: paths: ['cpdinput/**.cpd']`

### Quy Trình Tự Động (5 bước)

#### 1️⃣ Checkout Repository
- Clone code từ GitHub

#### 2️⃣ Process CPD Files  
```bash
calcpad-run cpdinput/file.cpd
```
- Xử lý tất cả file `.cpd` trong `cpdinput/`
- Tạo `file.html` trong `cpdinput/`
- Di chuyển sang `cpdoutput/file.html`

#### 3️⃣ Update Navigation Index
```python
python3 scripts/update_index.py
```
Tự động tạo `calcpad.html` với:
- ✅ Số thứ tự báo cáo
- ✅ Tên & tiêu đề
- ✅ Mô tả ngắn (phương pháp + kết quả + biểu đồ)
- ✅ Kích thước file
- ✅ Link trực tiếp
- ✅ Thời gian cập nhật

#### 4️⃣ Commit & Push
- Bot tự động commit kết quả: `Auto-generate reports [skip ci]`
- Push lên GitHub

#### 5️⃣ GitHub Pages Deploy
- File trong `cpdoutput/` tự động hiển thị trên GitHub Pages
- URLs:
  - GitHub: `https://hydrostructai.github.io/calcpad_engineering/calcpad.html`
  - Custom Domain: `https://hydrostructai.com/calcpad.html`

---

## 📝 Cách Sử Dụng

### Tạo báo cáo mới

1. Tạo file Calcpad (`.cpd`) trong thư mục `cpdinput/`:
```bash
cd calcpad_engineering
# Tạo hoặc sửa file .cpd
vim cpdinput/my_report.cpd
```

2. Commit & push
```bash
git add cpdinput/my_report.cpd
git commit -m "Add my_report analysis"
git push origin main
```

3. ✅ Workflow tự động:
- Xử lý file `my_report.cpd`
- Tạo `cpdoutput/my_report.html`
- Cập nhật `calcpad.html` với link mới
- Hiển thị trên web 🌐

---

## 📊 Thông Tin Metadata Tự Động Extract

Script `update_index.py` tự động:
- 📄 Lấy **tiêu đề** từ `<title>` tag
- 📐 Tìm **các phương pháp** từ heading `<h2>`
- 📊 Tìm **kết quả** từ heading  
- 📈 Đếm số **biểu đồ** (img tags)
- 💾 Lấy **kích thước file**

### Ví dụ Output Index
```
#1 biaxial_column
   📐 VIII. PHÂN TÍCH CHỊU UỐN ĐƠN TRỤC • 📊 VII. KIỂM TRA CHỊU UỐN XIÊN (BRESLER) • 📈 Có biểu đồ
   📄 35.5KB

#2 parametric_rc_beam  
   📐 PHƯƠNG PHÁP THIẾT KẾ DẦM BTCT • 📊 KẾT QUẢ VÀ KIỂM TRA • 📈 Có biểu đồ
   📄 35.2KB
```

---

## 🔧 Troubleshooting

### Workflow không chạy?
1. Kiểm tra file thật sự trong `cpdinput/`
2. Kiểm tra tên file: phải là `**.cpd`
3. Xem logs: https://github.com/hydrostructai/calcpad_engineering/actions

### HTML không được tạo?
1. Kiểm tra syntax `.cpd` file
2. Test local: `calcpad-run cpdinput/file.cpd`
3. Xem workflow logs chi tiết

### calcpad.html không cập nhật?
1. Chạy manual: `python3 scripts/update_index.py`
2. Kiểm tra file HTML đã được di chuyển đúng vị trí?
3. Git log check: Workflow có tạo commit?

---

## 📌 File Quan Trọng

| File | Mục đích |
|------|---------|
| `.github/workflows/main.yml` | Workflow automation |
| `scripts/update_index.py` | Index generator |
| `cpdinput/*.cpd` | Calcpad source files |
| `cpdoutput/*.html` | Generated reports |
| `calcpad.html` | Main index page |

---

## 🌐 Xem Báo Cáo

- **Local**: `file:///path/to/calcpad.html`
- **GitHub Pages**: https://hydrostructai.github.io/calcpad_engineering/calcpad.html
- **Custom Domain**: https://hydrostructai.com/calcpad.html (after DNS propagation)

