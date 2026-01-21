# Quick Reference Card

Fast lookup for common tasks and commands.

---

## 🚀 5-Minute Quick Start

### Add Your First Report
```bash
# 1. Copy CPD file to input folder
cp myanalysis.cpd calcpad_engineering/cpdinput/

# 2. Push to GitHub
cd calcpad_engineering
git add cpdinput/myanalysis.cpd
git commit -m "Add myanalysis"
git push origin main

# 3. Wait 2 minutes → Reports generated automatically
# Visit: https://hydrostructai.com/calcpad_engineering/calcpad.html
```

---

## 📋 Common Commands

### Adding Reports
```bash
git add cpdinput/file.cpd
git commit -m "Add report: Description"
git push origin main
```

### Checking Status
```bash
git status                           # Git status
git log --oneline -5               # Recent commits
ls -lh cpdoutput/*.html            # List HTML files
ls -lh cpdpdf/*.pdf                # List PDF files
```

### Regenerating Index
```bash
python3 scripts/update_index.py    # Regenerate index
git add calcpad.html
git commit -m "Regenerate index"
git push origin main
```

### Local Testing
```bash
python3 -m http.server 8000        # Start local server
# Open: http://localhost:8000/calcpad.html
```

---

## 📍 File Locations

| Type | Location | Example |
|------|----------|---------|
| **Input** | `cpdinput/` | `cpdinput/myfile.cpd` |
| **HTML** | `cpdoutput/` | `cpdoutput/myfile.html` |
| **PDF** | `cpdpdf/` | `cpdpdf/myfile.pdf` |
| **Index** | Root | `calcpad.html` |
| **Config** | `.github/workflows/` | `main.yml` |
| **Scripts** | `scripts/` | `update_index.py` |

---

## 🔗 Key URLs

| Link | Purpose |
|------|---------|
| https://hydrostructai.com | Main website |
| https://hydrostructai.com/calcpad_engineering/calcpad.html | All reports |
| https://github.com/hydrostructai/calcpad_engineering | Source code |
| https://github.com/hydrostructai/calcpad_engineering/actions | Workflow status |

---

## 📚 Documentation Guide

| Need | Read | Time |
|------|------|------|
| **Overview** | README.md | 5 min |
| **First report** | GETTING_STARTED.md | 15 min |
| **PDF help** | PDF_GENERATION.md | 10 min |
| **Architecture** | SYSTEM_SUMMARY.md | 10 min |
| **Navigation** | DOCUMENTATION_INDEX.md | 5 min |
| **Troubleshooting** | README.md → Troubleshooting | 5 min |

---

## ✅ Pre-Push Checklist

Before pushing your report:
- ✅ File is in `cpdinput/` folder
- ✅ File has `.cpd` extension
- ✅ Report title is descriptive
- ✅ No syntax errors in CPD file
- ✅ Commit message is clear
- ✅ Only pushing `.cpd` file (not generated files)

---

## 🔧 Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| **Workflow not running** | Check: https://github.com/hydrostructai/calcpad_engineering/actions |
| **HTML not generated** | Wait 2 minutes, refresh page, check Actions logs |
| **PDF missing** | Verify HTML generated first, check Actions for errors |
| **Index not updated** | Run: `python3 scripts/update_index.py` then push |
| **Domain not working** | Hard refresh (Ctrl+Shift+R), wait 5 minutes for DNS |
| **File not found** | Check folder: `ls cpdinput/` |

---

## 💡 Tips & Tricks

### Commit Messages
```bash
git commit -m "Add beam_analysis: Calculation for RC beam"
git commit -m "Update column_design: Fixed safety factors"
git commit -m "Fix slab_fea: Corrected mesh density"
```

### View File History
```bash
git log cpdinput/myfile.cpd    # All versions
git show abc123def              # Specific version
```

### Undo Changes
```bash
git restore cpdinput/file.cpd  # Discard local changes
git reset HEAD file.cpd        # Unstage file
git revert abc123              # Undo commit
```

### Check What Changed
```bash
git diff cpdinput/file.cpd     # See changes
git status                     # What's new
```

---

## 🎨 Customization

### Edit Report Title
In `.cpd` file, change first line:
```calcpad
"New Title - My Analysis"
```

### Add Description
Add comment lines starting with `\`:
```calcpad
"My Report"
\ This analyzes a reinforced concrete beam
\ Date: 2026-01-21
```

### Organize with Sections
```calcpad
"Main Report"

"Input Data"
L = 6

"Calculations"  
M = P * L / 4

"Results"
M = ? 
```

---

## 📊 Monitoring

### Check Latest Report
```bash
ls -lht cpdoutput/*.html | head -1   # Most recent HTML
ls -lht cpdpdf/*.pdf | head -1       # Most recent PDF
```

### Count Reports
```bash
ls cpdinput/*.cpd | wc -l    # Total CPD files
ls cpdoutput/*.html | wc -l  # Total HTML reports
ls cpdpdf/*.pdf | wc -l      # Total PDF reports
```

### Check Sizes
```bash
du -sh cpdoutput/    # Total HTML size
du -sh cpdpdf/       # Total PDF size
du -sh .             # Total repo size
```

---

## 🆘 Emergency Commands

### Reset Local Changes
```bash
git reset --hard origin/main
```

### See All Commits
```bash
git log --oneline --all
```

### Check Remote Status
```bash
git remote -v
git fetch --all
git status
```

### View Workflow Logs
```bash
# Open browser:
https://github.com/hydrostructai/calcpad_engineering/actions
# Click latest run, expand step for details
```

---

## 📞 Support Resources

**Internal Documentation:**
1. [README.md](README.md) - Overview
2. [GETTING_STARTED.md](GETTING_STARTED.md) - Guide
3. [PDF_GENERATION.md](PDF_GENERATION.md) - PDF help
4. [SYSTEM_SUMMARY.md](SYSTEM_SUMMARY.md) - Architecture
5. [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) - Navigation

**External Resources:**
- Calcpad: https://www.calcpad.eu/
- GitHub: https://docs.github.com/
- Git: https://git-scm.com/doc

---

## 🎯 Common Workflows

### Workflow: Add New Report
```
1. Create file: myreport.cpd
2. Run: git add cpdinput/myreport.cpd
3. Run: git commit -m "Add myreport: Description"
4. Run: git push origin main
5. Wait: 2 minutes
6. Visit: calcpad.html
7. Done! ✅
```

### Workflow: Update Existing Report
```
1. Edit: cpdinput/myreport.cpd
2. Run: git add cpdinput/myreport.cpd
3. Run: git commit -m "Update myreport: Changes"
4. Run: git push origin main
5. Wait: 2 minutes
6. Hard refresh: Ctrl+Shift+R
7. Done! ✅
```

### Workflow: Regenerate Index
```
1. Run: python3 scripts/update_index.py
2. Check: calcpad.html updated
3. Run: git add calcpad.html
4. Run: git commit -m "Regenerate index"
5. Run: git push origin main
6. Done! ✅
```

---

## ⚡ Performance Tips

### Keep Repository Lean
- Don't commit binary files
- Use `.gitignore` for temp files
- Archive old reports annually

### Optimize PDF Size
- Use `--dpi 150` instead of 300
- Compress images first
- Use `--image-quality 85`

### Fast Index Generation
- Python 3.8+ is faster
- Local testing is quicker
- Batch multiple reports

---

## 🔐 Security Notes

- ✅ All files in Git (version control)
- ✅ GitHub Actions has write permissions
- ✅ HTTPS enabled on website
- ✅ No sensitive data in reports
- ✅ Public repository

---

## 📋 Maintenance Tasks

### Daily
- Check for error emails from GitHub
- Monitor action logs if issues

### Weekly
- Review recent reports
- Test one report locally

### Monthly
- Archive completed reports
- Update documentation if needed
- Check disk space usage

---

## 🎓 Learning Resources

### For Calcpad
- Documentation: https://www.calcpad.eu/en/documentation/
- Examples: https://www.calcpad.eu/en/examples/
- Forum: https://www.calcpad.eu/forum/

### For GitHub Actions
- Documentation: https://docs.github.com/en/actions
- Examples: https://github.com/actions
- Marketplace: https://github.com/marketplace?type=actions

### For Git
- Tutorial: https://git-scm.com/doc
- Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

**Quick Reference v1.0 | 2026-01-21**

See [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) for complete documentation list.
