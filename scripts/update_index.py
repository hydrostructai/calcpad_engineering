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
        
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        elif tag == 'h1':
            self.in_h1 = True
        elif tag == 'h2':
            self.in_h2 = True
        elif tag == 'img':
            self.img_count += 1
    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag == 'h1':
            self.in_h1 = False
        elif tag == 'h2':
            self.in_h2 = False
    
    def handle_data(self, data):
        if self.in_title:
            self.title = data.strip()
        elif self.in_h1:
            if data.strip():
                self.h1_text = data.strip()
        elif self.in_h2:
            if data.strip() and len(self.h2_texts) < 5:
                self.h2_texts.append(data.strip())

def extract_metadata(html_path):
    """Extract metadata from HTML file"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        parser = HTMLMetadataExtractor()
        parser.feed(html_content)
        
        # Get file size
        file_size_kb = os.path.getsize(html_path) / 1024
        
        # Extract methods and results from h2 tags
        methods = []
        results = []
        for h2 in parser.h2_texts[:10]:
            if 'PHƯƠNG PHÁP' in h2 or 'CÔNG THỨC' in h2 or 'TÍNH TOÁN' in h2:
                methods.append(h2)
            elif 'KẾT QUẢ' in h2 or 'KIỂM TRA' in h2:
                results.append(h2)
        
        return {
            'title': parser.title or parser.h1_text or 'Report',
            'file_size': f"{file_size_kb:.1f}KB",
            'images': parser.img_count,
            'has_charts': parser.img_count > 0,
            'methods': methods[:2],
            'results': results[:2],
            'h2_list': parser.h2_texts[:5]
        }
    except Exception as e:
        print(f"Error extracting metadata from {html_path}: {e}")
        return {'title': 'Report', 'file_size': '0KB', 'images': 0, 'has_charts': False}

def get_pdf_size(pdf_path):
    """Get PDF file size"""
    try:
        if os.path.exists(pdf_path):
            return f"{os.path.getsize(pdf_path) / 1024:.1f}KB"
    except:
        pass
    return "0KB"

# Create output directories if needed
for dir_name in [output_dir, pdf_dir]:
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# Get list of HTML files with metadata
html_files = sorted([f for f in os.listdir(output_dir) if f.endswith('.html')])
reports = []

for idx, filename in enumerate(html_files, 1):
    filepath = os.path.join(output_dir, filename)
    metadata = extract_metadata(filepath)
    
    report_name = filename.replace(".html", "")
    
    # Check if corresponding PDF exists
    pdf_filename = f"{report_name}.pdf"
    pdf_path = os.path.join(pdf_dir, pdf_filename)
    has_pdf = os.path.exists(pdf_path)
    pdf_size = get_pdf_size(pdf_path) if has_pdf else "0KB"
    
    # Build description
    description_parts = []
    if metadata['methods']:
        description_parts.append(f"📐 {metadata['methods'][0]}")
    if metadata['results']:
        description_parts.append(f"📊 {metadata['results'][0]}")
    if metadata['has_charts']:
        description_parts.append("📈 Có biểu đồ")
    
    description = " • ".join(description_parts) if description_parts else "Báo cáo tính toán"
    
    reports.append({
        'index': idx,
        'filename': filename,
        'pdf_filename': pdf_filename if has_pdf else None,
        'name': report_name,
        'title': metadata['title'],
        'size': metadata['file_size'],
        'pdf_size': pdf_size,
        'has_pdf': has_pdf,
        'has_charts': metadata['has_charts'],
        'description': description,
        'sections': metadata['h2_list']
    })

# Generate table rows with description + links (no sizes)
links_html = ""
if reports:
    for report in reports:
        icon = "📈" if report.get('has_charts') else "📄"
        desc = report['description'] if report['description'] else report['title']
        links_html += f"""            <tr>
                <td style=\"padding:12px 10px; vertical-align:top;\">
                    <div style=\"font-size:1.5em; font-weight:700; display:flex; gap:10px; align-items:flex-start;\">
                        <span>{icon}</span>
                        <span>{report['title']}</span>
                    </div>
                    <div style=\"color:#7f8c8d; margin-top:6px;\">{desc}</div>
                </td>
                <td style=\"padding:12px 10px; vertical-align:top;\">
                    <a href=\"cpdoutput/{report['filename']}\" style=\"font-size:1.1em; font-weight:600;\">📄 HTML</a>
                </td>
                <td style=\"padding:12px 10px; vertical-align:top;\">
                    {f'<a href="cpdpdf/{report["pdf_filename"]}" style="font-size:1.1em; font-weight:600;">📕 PDF</a>' if report['has_pdf'] else '<span style="color:#bdc3c7;">📕 PDF</span>'}
                </td>
            </tr>
"""
else:
    links_html = "            <tr><td colspan=\"3\" style=\"padding:12px 10px;\">Chưa có báo cáo nào.</td></tr>"

# Create/update calcpad.html
template = f"""<!DOCTYPE html>
<html>
<head>
    <title>HydrostructAI - Calcpad Reports</title>
    <style>
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            margin: 0; 
            padding: 40px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        h1 {{ 
            color: #2c3e50; 
            border-bottom: 3px solid #3498db;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }}
        .report-count {{
            color: #7f8c8d;
            font-size: 0.95em;
            margin-bottom: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        thead th {{
            text-align: left;
            padding: 12px 10px;
            color: #2c3e50;
            border-bottom: 2px solid #ecf0f1;
            font-size: 0.95em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        tbody tr:nth-child(even) {{ background: #f8f9fa; }}
        tbody tr:hover {{
            background: #ecf0f1;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transform: translateX(4px);
        }}
        a {{ 
            text-decoration: none; 
            color: #3498db; 
            font-weight: bold;
            transition: color 0.3s ease;
        }}
        a:hover {{ 
            color: #2980b9;
            text-decoration: underline;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ecf0f1;
            color: #7f8c8d;
            font-size: 0.9em;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Danh sách báo cáo kỹ thuật</h1>
        <div class="report-count">Tổng cộng: <strong>{len(reports)}</strong> báo cáo | Cập nhật: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
        <table>
            <thead>
                <tr>
                    <th style="width:60%;">Nội dung tính toán</th>
                    <th style="width:20%;">HTML</th>
                    <th style="width:20%;">PDF</th>
                </tr>
            </thead>
            <tbody>
{links_html}            </tbody>
        </table>
        <div class="footer">
            <p>Calcpad Engineering Reports • <a href="https://hydrostructai.com" target="_blank">HydrostructAI</a> • Auto-generated by GitHub Actions</p>
            <p style="font-size: 0.85em;">📄 HTML (interactive) | 📕 PDF (printable)</p>
        </div>
    </div>
</body>
</html>
"""

with open(index_file, "w", encoding="utf-8") as f:
    f.write(template)

print(f"✅ Updated {index_file} with {len(reports)} reports")
