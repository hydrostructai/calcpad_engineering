# 🚀 Quick Start Guide - Upload CPD via GitHub Web

## ✅ Problem Fixed!

**Error**: `Permission to hydrostructai/calcpad_engineering.git denied to github-actions[bot]`

**Solution**: 
- ✅ Added `permissions: contents: write` to workflow
- ✅ Using `GITHUB_TOKEN` for authentication
- ✅ Proper error handling

---

## 📝 How to Upload CPD File via GitHub Web

### Method 1: Upload via GitHub Web Interface (Easy)

1. **Open GitHub**
   - Go to: https://github.com/hydrostructai/calcpad_engineering

2. **Navigate to cpdinput folder**
   - Click on `cpdinput` folder
   - Click "Add file" → "Upload files"

3. **Upload your .cpd file**
   - Drag & drop or select file
   - Click "Commit changes"
   - Write commit message (e.g., "Add my_report.cpd")
   - Click "Commit to main"

4. **✅ Automatic Processing**
   - GitHub Actions automatically triggers
   - Calcpad processes your file
   - HTML generated in `cpdoutput/`
   - `calcpad.html` index auto-updated
   - Results visible at: https://hydrostructai.github.io/calcpad_engineering/calcpad.html

---

## 🔄 Workflow Execution Flow

```
Upload .cpd to GitHub Web
         ↓
GitHub Actions Triggered
         ↓
Checkout Repository
         ↓
Process .cpd → Generate .html
         ↓
Move to cpdoutput/
         ↓
Run update_index.py
         ↓
Auto-commit with GITHUB_TOKEN
         ↓
Push to main (with write permission)
         ↓
GitHub Pages Updated
         ↓
View at: hydrostructai.github.io/calcpad_engineering/calcpad.html
```

---

## 🎯 What Happens Automatically

When you upload a `.cpd` file:

| Step | Action | Result |
|------|--------|--------|
| 1 | Upload `report.cpd` to `cpdinput/` | File stored in repo |
| 2 | GitHub Actions triggers | Workflow starts |
| 3 | `calcpad-run report.cpd` | `report.html` generated |
| 4 | Move to `cpdoutput/` | Ready for GitHub Pages |
| 5 | Extract metadata | Get title, methods, results, charts |
| 6 | Update `calcpad.html` | Add new report with: |
|   |  | - Report number (#1, #2, ...) |
|   |  | - Report name & title |
|   |  | - Methods & results info |
|   |  | - File size |
|   |  | - Direct link |
| 7 | Auto-commit | `Auto-generate reports [skip ci]` |
| 8 | Push to GitHub | Updates main branch |
| 9 | Deploy to Pages | Live at website URL |

---

## 📊 View Your Reports

After upload completes (usually 1-2 minutes):

- **GitHub Pages**: https://hydrostructai.github.io/calcpad_engineering/calcpad.html
- **Custom Domain**: https://hydrostructai.com/calcpad.html (after DNS propagation)

Each report shows:
- ✅ Report number
- ✅ File name as link
- ✅ Calculation method used
- ✅ Results section info
- ✅ Chart indication
- ✅ File size

---

## 🔍 Check Workflow Status

1. Go to: https://github.com/hydrostructai/calcpad_engineering/actions
2. Click on latest workflow run
3. View step-by-step execution
4. Check for ✅ (success) or ❌ (error)

---

## ⚠️ Troubleshooting

### Workflow doesn't trigger?
- Confirm file is in `cpdinput/` folder
- File name must end with `.cpd`
- Check if path filter matches

### HTML not generated?
- Check `.cpd` file syntax
- View workflow logs for error details
- Test locally: `calcpad-run cpdinput/file.cpd`

### Push permission error?
- Should be fixed now (GITHUB_TOKEN permissions added)
- Check workflow permissions in repository settings
- Verify `permissions: contents: write` in workflow YAML

### calcpad.html not updating?
- Confirm HTML exists in `cpdoutput/`
- Run manually: `python3 scripts/update_index.py`
- Check git commit: `git log --oneline`

---

## 📌 Key Files

| File | Purpose |
|------|---------|
| `.github/workflows/main.yml` | Workflow configuration |
| `scripts/update_index.py` | Auto-generate index |
| `cpdinput/*.cpd` | Your report source files |
| `cpdoutput/*.html` | Generated reports |
| `calcpad.html` | Main index page |

---

## 💡 Tips

✅ **Best Practices**:
- Use descriptive file names: `analysis_2026.cpd`
- Write clear calculation comments in .cpd
- Include section headings (h2) for metadata extraction
- Add charts/plots for better reports

✅ **File Size**:
- Typical report: 30-50 KB
- All reports listed on one index page
- No size limit imposed

✅ **Automation**:
- No manual HTML generation needed
- No manual index updates needed
- No manual deployment needed
- Just upload and wait! 🎉

---

## 📞 Need Help?

- Check `WORKFLOW_GUIDE.md` for detailed documentation
- Review workflow logs: GitHub Actions tab
- Test locally before uploading
- Verify .cpd syntax with Calcpad locally

**Status**: ✅ Ready to use!
