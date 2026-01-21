# GitHub Actions Automation Flow

## 🎯 How Calcpad Reports Are Auto-Published

When you add a `.cpd` file to the system, GitHub Actions automatically converts it to HTML and PDF, then updates the index page. Here's the complete workflow:

---

## 📋 Step-by-Step Process

### Step 1: File Detection
```
User saves .cpd file in cpdinput/ folder
    ↓
GitHub detects file change
    ↓
GitHub Actions workflow triggers automatically
```

### Step 2: HTML Generation
```
GitHub Actions downloads the .cpd file
    ↓
Runs Calcpad command-line tool
    ↓
Command: calcpad cpdinput/filename.cpd
    ↓
Generates: filename.html (interactive report)
```

### Step 3: PDF Conversion
```
Takes generated filename.html
    ↓
Runs PDF converter (wkhtmltopdf)
    ↓
Command: wkhtmltopdf cpdoutput/filename.html cpdpdf/filename.pdf
    ↓
Generates: filename.pdf (printable version)
```

### Step 4: Index Update
```
Scans cpdoutput/ folder for all .html files
    ↓
Scans cpdpdf/ folder for all .pdf files
    ↓
Runs Python script: update_index.py
    ↓
Extracts metadata from each HTML report:
  - Report title (from HTML header)
  - File sizes
  - Description (if available)
    ↓
Updates calcpad.html index page with:
  - Links to HTML reports
  - Links to PDF reports
  - Report information
  - Dynamic report count
```

### Step 5: Auto-Commit & Deploy
```
All changes made (HTML, PDF, updated index)
    ↓
GitHub Actions commits changes automatically
    ↓
Commit message: "Auto-generate reports: HTML + PDF [skip ci]"
    ↓
Pushes to GitHub repository
    ↓
GitHub Pages automatically deploys
    ↓
Reports live on website within 1-2 minutes
```

---

## 🔍 What Gets Updated in calcpad.html

Each time a new `.cpd` file is processed, the index page (`calcpad.html`) is updated with:

### Report List Entry
```html
<li>
    <span>#1, #2, #3...</span>           <!-- Auto-numbered -->
    <a href="cpdoutput/filename.html">📄 HTML</a>
    <a href="cpdpdf/filename.pdf">📕 PDF</a>
    <strong>Report Title</strong>        <!-- Extracted from HTML -->
    <div>Description or details</div>    <!-- From metadata -->
    <div>📊 HTML: 43.2KB | 📕 PDF: 25.2KB</div>  <!-- File sizes -->
</li>
```

### Dynamic Report Count
```javascript
// JavaScript automatically counts report items
const reportCount = document.querySelectorAll('li').length;
document.getElementById('report-count').textContent = reportCount;
```

---

## ⚙️ Technical Details

### Trigger Event
- **When:** File pushed to `cpdinput/*.cpd`
- **Condition:** Path matches `.cpd` file extension
- **Runner:** Ubuntu latest

### Tools Used
1. **Calcpad CLI v7.5.9**
   - Command: `calcpad cpdinput/file.cpd`
   - Output: `file.html` (interactive web report)

2. **wkhtmltopdf**
   - Command: `wkhtmltopdf cpdoutput/file.html cpdpdf/file.pdf`
   - Output: `file.pdf` (printable document)

3. **Python 3 (update_index.py)**
   - Extracts HTML metadata
   - Counts files in directories
   - Generates updated `calcpad.html`

4. **Git**
   - Auto-commits changes
   - Pushes to repository
   - Triggered by workflow bot

---

## 📊 File Flow Diagram

```
cpdinput/
  ├─ filename.cpd (your input)
  │   ↓ [Calcpad processes]
  │
cpdoutput/
  ├─ filename.html (interactive)
  │
cpdpdf/
  ├─ filename.pdf (printable)
  │
calcpad.html (index page)
  ├─ Updated with new report
  ├─ New HTML link added
  ├─ New PDF link added
  ├─ Report count incremented
  └─ Ready to view
```

---

## 🎯 Key Points

✅ **Fully Automatic**
- No manual steps required
- Triggers on file detection
- Completes in ~2 minutes

✅ **Report Format Support**
- HTML (interactive, responsive)
- PDF (printable, shareable)
- Both generated simultaneously

✅ **Index Management**
- Automatic title extraction
- File size tracking
- Dynamic report counting
- Report links always working

✅ **Error Handling**
- Invalid `.cpd` files caught
- Syntax errors reported
- Failed builds won't deploy

---

## 🔄 Workflow Configuration

The automation is configured in:
- **Location:** `.github/workflows/main.yml`
- **Trigger:** Push to `cpdinput/*.cpd`
- **Permissions:** Read/Write access
- **Concurrency:** One job at a time

---

## 📝 How Index Count Updates

### Before (Hard-coded)
```html
<div>Tổng cộng: <strong>4</strong> báo cáo</div>
```
Problem: Needs manual update when reports added

### After (Dynamic)
```html
<div>Tổng cộng: <strong id="report-count">4</strong> báo cáo</div>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const count = document.querySelectorAll('li').length;
        document.getElementById('report-count').textContent = count;
    });
</script>
```
Benefit: Updates automatically based on actual reports in page

---

## 🚀 Quick Reference

| Task | What Happens |
|------|--------------|
| Add `.cpd` file | GitHub Actions automatically triggered |
| Calcpad processes | HTML created in ~30 seconds |
| PDF generation | PDF created in ~20 seconds |
| Index updates | `calcpad.html` regenerated automatically |
| Deploy ready | Reports live on website in ~1 minute |

---

## 📞 Troubleshooting

### Report Not Appearing
1. Check file is in `cpdinput/` folder
2. Verify file extension is `.cpd`
3. Ensure no syntax errors in `.cpd`
4. Wait 1-2 minutes for automation to complete

### HTML/PDF Missing
1. Check workflow logs for errors
2. Verify Calcpad syntax is valid
3. Ensure PDF converter is working
4. Check file permissions

### Index Not Updating
1. Verify HTML file was created
2. Check Python script ran successfully
3. Ensure JavaScript enabled in browser
4. Refresh page (Ctrl+F5)

---

## 📚 For Developers

### Location of Automation Files
- `.github/workflows/main.yml` - Workflow definition
- `scripts/update_index.py` - Index generation script
- `calcpad.html` - Index template

### How to Extend
- Add more file types: Modify workflow trigger path
- Custom report names: Update metadata extraction
- Different styling: Edit HTML template
- Additional metadata: Modify Python script

---

**Last Updated:** 2026-01-22
