import os

output_dir = "cpdoutput"
index_file = "calcpad.html"

# Lấy danh sách file html
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
links_html = "".join([f'<li><a href="cpdoutput/{f}">{f.replace(".html", "")}</a></li>' for f in files])

# Cập nhật file calcpad.html
template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>HydrostructAI - Calcpad Reports</title>
    <style>
        body {{ font-family: sans-serif; margin: 40px; line-height: 1.6; }}
        h1 {{ color: #2c3e50; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ background: #f4f4f4; margin: 10px 0; padding: 15px; border-radius: 5px; }}
        a {{ text-decoration: none; color: #3498db; font-weight: bold; }}
        a:hover {{ color: #2980b9; }}
    </style>
</head>
<body>
    <h1>Danh sách báo cáo kỹ thuật</h1>
    <ul>
        {links_html if links_html else '<li>Chưa có báo cáo nào.</li>'}
    </ul>
</body>
</html>
"""

with open(index_file, "w", encoding="utf-8") as f:
    f.write(template)
