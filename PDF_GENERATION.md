# PDF Generation Feature

## Overview

When you upload a `.cpd` file to GitHub, the workflow automatically generates **both HTML and PDF** versions:

```
Input:  file.cpd
         ↓
Output: cpdoutput/file.html  (interactive, web-viewable)
        cpdpdf/file.pdf      (printable, offline-viewable)
```

---

## Features

### Automatic PDF Generation
- ✅ Triggered automatically when `.cpd` file is pushed
- ✅ Uses `wkhtmltopdf` to convert HTML → PDF
- ✅ PDF stored in `/cpdpdf/` folder
- ✅ Both files linked in `calcpad.html` index

### Dual Format Support
**HTML Version:**
- 📊 Interactive plots and visualizations
- 🔗 Clickable navigation
- 📱 Responsive design
- 🌐 View in any browser

**PDF Version:**
- 🖨️ Print-optimized layout
- 📄 Standalone document
- 💾 Download and archive
- ✏️ Annotate and mark up

### Smart Index
The `calcpad.html` automatically displays:
- ✅ Both HTML and PDF download links
- ✅ File sizes for each format
- ✅ Report metadata and description
- ✅ Download status (grayed out if not yet generated)

---

## How It Works

### Workflow Steps

**1. Process CPD Files:**
```bash
calcpad file.cpd
→ Generates: cpdinput/file.html
```

**2. Move to Output:**
```bash
mv cpdinput/file.html cpdoutput/file.html
```

**3. Convert to PDF:**
```bash
wkhtmltopdf cpdoutput/file.html cpdpdf/file.pdf
```

**4. Update Index:**
```python
python3 scripts/update_index.py
→ Regenerates: calcpad.html with both links
```

**5. Auto-Commit & Push:**
```bash
git add cpdoutput/*.html cpdpdf/*.pdf calcpad.html
git commit -m "Auto-generate reports: HTML + PDF [skip ci]"
git push origin main
```

---

## Folder Structure

```
calcpad_engineering/
├── cpdinput/              # Source .cpd files
│   ├── file1.cpd
│   └── file2.cpd
│
├── cpdoutput/             # Generated HTML (interactive)
│   ├── file1.html
│   └── file2.html
│
├── cpdpdf/                # Generated PDF (printable) ← NEW!
│   ├── file1.pdf
│   └── file2.pdf
│
└── calcpad.html           # Index with dual links ← UPDATED!
```

---

## Index Structure

### Before (HTML Only)
```html
#1 biaxial_column
   📄 HTML: 34.6KB
   → cpdoutput/biaxial_column.html
```

### After (HTML + PDF)
```html
#1 biaxial_column
   📄 HTML  |  📕 PDF
   📊 HTML: 34.6KB  |  PDF: 120KB
   → cpdoutput/biaxial_column.html
   → cpdpdf/biaxial_column.pdf
```

---

## Using PDF Files

### Download & View
1. Open: https://hydrostructai.github.io/calcpad_engineering/calcpad.html
2. Click "📕 PDF" link for any report
3. View in browser or save locally

### Print Report
1. Open PDF link
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Save as PDF or print to physical printer

### Archive & Backup
```bash
# Download all PDFs
mkdir -p local_reports
for report in https://hydrostructai.github.io/calcpad_engineering/cpdpdf/*.pdf
do
  wget "$report" -P local_reports/
done
```

### Share Reports
- Share HTML link for interactive viewing
- Share PDF link for offline/print sharing
- Both formats in one index

---

## PDF Options (Customizable)

The workflow uses `wkhtmltopdf` with quiet mode:
```bash
wkhtmltopdf --quiet source.html output.pdf
```

To customize PDF generation (in workflow), edit:
```yaml
wkhtmltopdf --quiet \
  --page-size A4 \
  --dpi 150 \
  --print-media-type \
  "cpdoutput/$filename.html" \
  "cpdpdf/$filename.pdf"
```

Options available:
- `--page-size`: A4, Letter, Legal, etc.
- `--dpi`: 72, 150, 300 (quality)
- `--print-media-type`: Use CSS print styles
- `--margin-*`: Top, Bottom, Left, Right margins
- `--header-*`: Add header/footer

---

## Storage Considerations

### File Sizes
- **Typical HTML**: 30-50 KB (interactive)
- **Typical PDF**: 100-200 KB (static)
- **For 10 reports**: ~2.5 MB total

### Git Repository
- PDFs are version controlled in Git
- Large file storage note: PDFs grow repo size
- Alternative: Use Git LFS for PDFs (optional)

### Disable PDF (Optional)
If you want HTML-only, comment out PDF generation:
```yaml
# Convert HTML to PDF
# if command -v wkhtmltopdf &> /dev/null; then
#   wkhtmltopdf --quiet ...
```

---

## Troubleshooting

### "PDF generation failed"
**Cause:** `wkhtmltopdf` not available on GitHub runners

**Solution:** It's installed on Ubuntu runners by default
- If missing, workflow skips PDF silently
- HTML still generates normally
- Check workflow logs for details

### "PDF file empty"
**Cause:** HTML has broken resources (images, fonts)

**Solution:**
1. Check HTML file first - does it load in browser?
2. Ensure all assets are self-contained
3. Test locally: `wkhtmltopdf test.html test.pdf`

### "PDF very large file"
**Cause:** Many embedded images/charts

**Solution:**
- Use `--dpi 150` instead of 300 (faster, smaller)
- Compress images in HTML first
- Add `--image-quality 85` to reduce quality

### "PDF links not clickable"
**Cause:** Some HTML links may not work in PDF

**Solution:**
- Use `--enable-local-file-access` flag
- Most interactive content won't work in PDF (by design)

---

## Integration with GitHub Pages

Both HTML and PDF are deployed to GitHub Pages:
- 🌐 **HTML**: `hydrostructai.github.io/calcpad_engineering/cpdoutput/`
- 📕 **PDF**: `hydrostructai.github.io/calcpad_engineering/cpdpdf/`
- 📊 **Index**: `hydrostructai.github.io/calcpad_engineering/calcpad.html`

All files are:
- ✅ Publicly accessible
- ✅ Automatically updated
- ✅ Version controlled in Git

---

## Workflow Permissions

The workflow requires:
```yaml
permissions:
  contents: write  # Write HTML + PDF to repo
```

This allows GitHub Actions bot to:
- ✅ Generate PDFs
- ✅ Commit files
- ✅ Push to main branch

---

## Best Practices

✅ **Do:**
- Keep PDF generation settings consistent
- Archive old PDFs with report versions
- Document PDF layout in CPD comments
- Test HTML rendering before PDF generation

❌ **Don't:**
- Upload PDFs manually (use automation!)
- Disable PDF feature for production reports
- Use PDF as source of truth (use CPD files)
- Commit PDFs without HTML alternatives

---

## Next Steps

1. **Push a new .cpd file**
   ```bash
   git add cpdinput/myreport.cpd
   git commit -m "Add report"
   git push origin main
   ```

2. **Wait 1-2 minutes** for GitHub Actions

3. **Check results:**
   - HTML: `calcpad.html` shows "📄 HTML" link
   - PDF: `calcpad.html` shows "📕 PDF" link

4. **Download or view:**
   - Click links in `calcpad.html` index
   - Or access directly:
     - `cpdoutput/myreport.html`
     - `cpdpdf/myreport.pdf`

---

## Architecture Summary

```
Push .cpd
   ↓
GitHub Actions Workflow Triggered
   ↓
[1] calcpad file.cpd → HTML
[2] Move → cpdoutput/
[3] wkhtmltopdf HTML → PDF
[4] Move → cpdpdf/
[5] python3 scripts/update_index.py
[6] Auto-commit (HTML + PDF + index)
[7] Auto-push to main
   ↓
GitHub Pages Updated
   ↓
calcpad.html displays both formats
   ↓
✨ Done! Users can view/download both versions
```

---

## Configuration Files

Updated Files:
- `.github/workflows/main.yml` - Added PDF generation step
- `scripts/update_index.py` - Added PDF link support
- `calcpad.html` - Updated to show dual links
- `.gitignore` - Added PDF-related entries

New Folders:
- `cpdpdf/` - PDF output directory

---

## Support

For issues:
1. Check GitHub Actions logs: https://github.com/hydrostructai/calcpad_engineering/actions
2. Review workflow output for errors
3. Test locally: `wkhtmltopdf test.html test.pdf`
4. Verify permissions in repository settings
