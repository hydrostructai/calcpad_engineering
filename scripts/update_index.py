import os
import re
from html.parser import HTMLParser
from datetime import datetime
from pathlib import Path

output_dir = "cpdoutput"
pdf_dir = "cpdpdf"
index_file = "calcpad.html"

class HTMLMetadataExtractor(HTMLParser):
    """Extract title and summary from Calcpad HTML reports"""
    def __init__(self):
        super().__init__()
        self.title = ""
        self.h1_text = ""
        self.h2_texts = []
        self.in_h1 = False
        self.in_h2 = False
        self.in_title = False
        self.img_count = 0
        self.paragraphs = []
        self.in_p = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        elif tag == 'h1':
            self.in_h1 = True
        elif tag == 'h2':
            self.in_h2 = True
        elif tag == 'p':
            self.in_p = True
        elif tag == 'img':
            self.img_count += 1
    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag == 'h1':
            self.in_h1 = False
        elif tag == 'h2':
            self.in_h2 = False
        elif tag == 'p':
            self.in_p = False
    
    def handle_data(self, data):
        data = data.strip()
        if not data:
            return
            
        if self.in_title:
            self.title = data
        elif self.in_h1:
            self.h1_text = data
        elif self.in_h2:
            if len(self.h2_texts) < 10:
                self.h2_texts.append(data)
        elif self.in_p:
            if len(self.paragraphs) < 5:
                self.paragraphs.append(data)

def extract_metadata(html_path):
    """Extract metadata from HTML file"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        parser = HTMLMetadataExtractor()
        parser.feed(html_content)
        
        # Determine the best title/description
        main_title = parser.h1_text or parser.title or Path(html_path).stem.replace('_', ' ').title()
        
        # Summary description
        summary = ""
        if parser.paragraphs:
            summary = parser.paragraphs[0]
        elif parser.h2_texts:
            summary = " • ".join(parser.h2_texts[:2])
            
        if not summary:
            summary = "Báo cáo tính toán kỹ thuật"
        
        # FIX: If title is generic "Created with Calcpad", use summary or filename
        if "Created with Calcpad" in main_title or main_title.lower() == "calcpad":
            if summary and len(summary) > 5 and "Báo cáo" not in summary:
                main_title = summary
                summary = "" # Clear summary so it doesn't repeat
            else:
                main_title = Path(html_path).stem.replace('_', ' ').title()
        
        # Logic for icons
        icon = "📊"
        lower_title = main_title.lower()
        if "beam" in lower_title or "dầm" in lower_title:
            icon = "📏"
        elif "column" in lower_title or "cột" in lower_title:
            icon = "🏛️"
        elif "slab" in lower_title or "sàn" in lower_title:
            icon = "🧱"
        elif "mesh" in lower_title:
            icon = "🕸️"
        elif "pi" in lower_title or "monte" in lower_title:
            icon = "🎲"
        elif "section" in lower_title:
            icon = "📐"
        elif parser.img_count > 0:
            icon = "📈"

        return {
            'title': main_title,
            'description': summary,
            'icon': icon,
            'has_charts': parser.img_count > 0
        }
    except Exception as e:
        print(f"Error extracting metadata from {html_path}: {e}")
        return {
            'title': Path(html_path).stem,
            'description': 'Báo cáo kỹ thuật',
            'icon': '📄',
            'has_charts': False
        }

# Create output directories if needed
for dir_name in [output_dir, pdf_dir]:
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# Get list of HTML files from cpdoutput directory
try:
    html_files = sorted([f for f in os.listdir(output_dir) if f.endswith('.html')])
    print(f"Found {len(html_files)} HTML files in {output_dir}/")
except FileNotFoundError:
    print(f"❌ Error: Directory {output_dir}/ not found")
    html_files = []

reports = []

for filename in html_files:
    filepath = os.path.join(output_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"⚠️  Skipping {filename} - file not found")
        continue
    
    print(f"  📄 Processing: {filename}")
    metadata = extract_metadata(filepath)
    
    report_name = filename.replace(".html", "")
    
    # Check if corresponding PDF exists
    pdf_filename = f"{report_name}.pdf"
    pdf_path = os.path.join(pdf_dir, pdf_filename)
    has_pdf = os.path.exists(pdf_path)
    
    if has_pdf:
        print(f"     ✓ Found matching PDF: {pdf_filename}")
    else:
        print(f"     ⚠ No PDF found for: {report_name}")
    
    # Get file modification time
    mtime = os.path.getmtime(filepath)
    formatted_time = datetime.fromtimestamp(mtime).strftime('%d/%m/%Y %H:%M')
    
    reports.append({
        'filename': filename,
        'pdf_filename': pdf_filename if has_pdf else None,
        'title': metadata['title'],
        'description': metadata['description'],
        'icon': metadata['icon'],
        'has_pdf': has_pdf,
        'created_time': formatted_time
    })

print(f"\n📊 Total reports collected: {len(reports)}")

# Generate table rows
links_html = ""
if reports:
    for report in reports:
        pdf_link = f'<a href="cpdpdf/{report["pdf_filename"]}" class="btn-pdf">📕 PDF</a>' if report['has_pdf'] else '<span class="no-pdf">📕 (N/A)</span>'
        
        summary_html = f'<div class="report-summary">{report["description"]}</div>' if report["description"] else ''
        
        links_html += f"""            <tr>
                <td class="col-desc">
                    <a href="cpdoutput/{report['filename']}" style="text-decoration: none;">
                        <div class="report-title">{report['icon']} {report['title']}</div>
                    </a>
                    {summary_html}
                </td>
                <td class="col-link">
                    {pdf_link}
                </td>
                <td style="text-align: center; color: var(--text-muted); font-size: 0.85rem;">
                    {report['created_time']}
                </td>
            </tr>
"""
else:
    links_html = '            <tr><td colspan="3" style="padding:40px; text-align:center; color:#95a5a6;">Chưa có báo cáo nào được tạo.</td></tr>'

# Create/update calcpad.html
template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HydrostructAI - Calcpad Engineering Reports</title>
    <style>
        :root {{
            --primary: #2563eb;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --border: #e2e8f0;
        }}
        body {{ 
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            margin: 0; 
            padding: 20px;
            background-color: var(--bg);
            color: var(--text-main);
            line-height: 1.5;
        }}
        .container {{
            max-width: 1100px;
            margin: 40px auto;
            background: var(--card-bg);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        }}
        header {{
            border-bottom: 2px solid var(--border);
            margin-bottom: 30px;
            padding-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }}
        h1 {{ 
            margin: 0;
            color: var(--text-main);
            font-size: 2rem;
            font-weight: 800;
        }}
        .stats {{
            color: var(--text-muted);
            font-size: 0.9rem;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        th {{
            text-align: left;
            padding: 15px;
            background: #f1f5f9;
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.05em;
        }}
        tr {{
            border-bottom: 1px solid var(--border);
            transition: background 0.2s;
        }}
        tr:hover {{
            background-color: #f8fafc;
        }}
        td {{
            padding: 20px 15px;
            vertical-align: middle;
        }}
        .col-desc {{ width: 60%; }}
        .col-link {{ width: 20%; text-align: center; }}
        
        .report-title {{
            font-size: 1.5rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .report-summary {{
            color: var(--text-muted);
            font-size: 0.95rem;
        }}
        
        .btn-html, .btn-pdf {{
            display: inline-flex;
            align-items: center;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
            font-size: 0.9rem;
        }}
        .btn-html {{
            background: #eff6ff;
            color: #1d4ed8;
        }}
        .btn-html:hover {{
            background: #dbeafe;
        }}
        .btn-pdf {{
            background: #fff1f2;
            color: #e11d48;
        }}
        .btn-pdf:hover {{
            background: #ffe4e6;
        }}
        .no-pdf {{
            color: #cbd5e1;
            font-size: 0.9rem;
            font-weight: 500;
        }}
        
        .footer {{
            margin-top: 50px;
            text-align: center;
            padding-top: 30px;
            border-top: 1px solid var(--border);
            font-size: 0.85rem;
            color: var(--text-muted);
        }}
        .footer a {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
        }}
        
        @media (max-width: 768px) {{
            .container {{ padding: 20px; }}
            .report-title {{ font-size: 1.2rem; }}
            th, td {{ padding: 10px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div>
                <h1>📊 MỘT SỐ KẾT QUẢ TÍNH TOÁN SỬ DỤNG CALCPAD</h1>
                <div class="stats">HydrostructAI Engineering Excellence</div>
            </div>
            <div style="text-align: right;">
                <strong style="font-size: 1.2em;">{len(reports)}</strong> items<br>
                <small>Updated: {datetime.now().strftime('%d/%m/%Y %H:%M')}</small>
            </div>
        </header>

        <section style="margin-bottom: 40px; padding: 25px; background: #f8fafc; border-radius: 12px; border: 1px solid var(--border);">
            <h2 style="margin-top: 0; color: var(--text-main); font-size: 1.4rem; display: flex; align-items: center; gap: 10px;">
                📖 TÀI LIỆU HƯỚNG DẪN CALCPAD
            </h2>
            <p style="color: var(--text-muted); margin-bottom: 20px;">
                Hướng dẫn chi tiết về cách thiết lập, sử dụng và tối ưu hóa các báo cáo tính toán Calcpad cho kỹ thuật.
            </p>
            <a href="https://hydrostructai.com/calcpad_engineering" style="display: inline-flex; align-items: center; gap: 10px; padding: 12px 24px; background: var(--primary); color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: opacity 0.2s;">
                🌐 TRUY CẬP TÀI LIỆU HƯỚNG DẪN
            </a>
        </section>
        
        <h2 style="font-size: 1.5rem; margin-bottom: 20px; color: var(--text-main); display: flex; align-items: center; gap: 10px;">
            📋 NỘI DUNG TÍNH TOÁN
        </h2>
        
        <table>
            <thead>
                <tr>
                    <th>NỘI DUNG TÍNH TOÁN</th>
                    <th style="text-align: center;">PDF</th>
                    <th style="text-align: center;">THỜI ĐIỂM TẠO</th>
                </tr>
            </thead>
            <tbody>
{links_html}            </tbody>
        </table>
        
        <div class="footer">
            <p>
                Powered by <a href="https://calcpad.eu" target="_blank">Calcpad</a> & 
                <a href="https://github.com/Proektsoftbg/Calcpad" target="_blank">Proektsoftbg</a>
            </p>
            <p>© {datetime.now().year} <a href="https://hydrostructai.com" target="_blank">HydrostructAI</a>. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
"""

with open(index_file, "w", encoding="utf-8") as f:
    f.write(template)

print(f"✅ Updated {index_file} successfully")
