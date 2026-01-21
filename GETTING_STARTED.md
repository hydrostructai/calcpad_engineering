# Getting Started Guide

Quick reference for common tasks with the Calcpad Engineering automation system.

---

## 📌 First Time Setup (5 minutes)

### 1. Clone Repository
```bash
git clone https://github.com/hydrostructai/calcpad_engineering.git
cd calcpad_engineering
```

### 2. Check Your Git Configuration
```bash
git config user.name    # Should show your name
git config user.email   # Should show your email
```

If not set:
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 3. Verify Repository Structure
```bash
ls -la
# Should see: cpdinput/ cpdoutput/ cpdpdf/ scripts/ .github/ calcpad.html
```

### 4. You're Ready! 🎉

---

## ➕ Add Your First Report (2 minutes)

### Quick Method

**Step 1: Create or copy your `.cpd` file**
```bash
# Either create new:
cat > cpdinput/my_analysis.cpd << 'EOF'
"My First Analysis"
x = 10 "Input value"
y = x * 2
y = ? "Output value"
EOF

# Or copy existing:
cp ~/Downloads/myanalysis.cpd cpdinput/
```

**Step 2: Push to GitHub**
```bash
git add cpdinput/my_analysis.cpd
git commit -m "Add my_analysis: Description of what this does"
git push origin main
```

**Step 3: Wait 1-2 minutes**

GitHub Actions will:
- ✅ Generate HTML report
- ✅ Generate PDF report
- ✅ Update index automatically

**Step 4: View Your Report**

Visit: https://hydrostructai.com/calcpad_engineering/calcpad.html

You should see your report with both 📄 HTML and 📕 PDF links!

---

## 🔍 Check Report Status

### View Latest Workflow Run

```bash
# Option 1: GitHub Web
# Visit: https://github.com/hydrostructai/calcpad_engineering/actions
# Click latest run and review logs

# Option 2: Local Git Log
git log --oneline -10
# Should show your "Add" commit

# Option 3: Check Generated Files
ls -lh cpdoutput/ cpdpdf/
# Should see your newly generated files
```

### Verify Generated Files

```bash
# Check if HTML was generated
ls -lh cpdoutput/my_analysis.html

# Check if PDF was generated
ls -lh cpdpdf/my_analysis.pdf

# Check index was updated
grep "my_analysis" calcpad.html
```

---

## ✏️ Edit Existing Report

### Modify CPD File

```bash
# Edit the file
nano cpdinput/my_analysis.cpd

# Or use your preferred editor
code cpdinput/my_analysis.cpd

# Make changes and save
```

### Push Updated Version

```bash
git add cpdinput/my_analysis.cpd
git commit -m "Update my_analysis: Fixed calculation, improved clarity"
git push origin main
```

The workflow will:
- Regenerate HTML with your changes
- Regenerate PDF with your changes
- Update links in index

### View Updated Report

Visit: https://hydrostructai.com/calcpad_engineering/calcpad.html

Hard refresh browser (Ctrl+F5) to see latest version.

---

## 📥 Manually Regenerate Index

If you need to regenerate the index locally:

```bash
python3 scripts/update_index.py
```

Output:
```
✅ Updated calcpad.html with X reports
```

Then commit and push:
```bash
git add calcpad.html
git commit -m "Regenerate index"
git push origin main
```

---

## 🐛 Common Issues

### Issue: "File not found" error

**Problem:** Can't find file to edit

**Solution:**
```bash
# Check file exists
ls cpdinput/

# List all .cpd files
ls cpdinput/*.cpd

# Create folder if missing
mkdir -p cpdinput/
```

---

### Issue: "Nothing changed" after push

**Problem:** Report wasn't updated on website

**Solution:**
```bash
# 1. Hard refresh browser
# Press: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)

# 2. Check if file was actually committed
git log cpdinput/myfile.cpd

# 3. Verify GitHub Actions ran
# Visit: https://github.com/hydrostructai/calcpad_engineering/actions

# 4. Check files generated locally
ls -lh cpdoutput/myfile.html
ls -lh cpdpdf/myfile.pdf
```

---

### Issue: "Git permission denied"

**Problem:** Can't push to GitHub

**Solution:**
```bash
# Check you have write access
git remote -v
# Should show: origin https://github.com/hydrostructai/calcpad_engineering.git

# Check your git credentials are saved
git config --global credential.helper store

# Try pushing again
git push origin main

# If still fails, create Personal Access Token:
# https://github.com/settings/tokens
```

---

### Issue: "PDF not generated"

**Problem:** HTML works but PDF link is missing

**Solution:**
```bash
# 1. Check workflow logs
# Visit: https://github.com/hydrostructai/calcpad_engineering/actions
# Look for any error messages

# 2. Test locally
wkhtmltopdf cpdoutput/myfile.html cpdpdf/myfile.pdf

# 3. If error, check if file exists
ls -lh cpdoutput/myfile.html

# 4. If HTML missing, check Calcpad worked
# Look at workflow logs for Calcpad errors
```

---

## 🎨 Customization Examples

### Change Report Title

Edit the first line of `.cpd`:

```calcpad
"New Title - My Structural Analysis"
x = 10
...
```

### Add Description

Add comment lines (start with `\`):

```calcpad
"My Report"
\ This is a structural analysis for a RC beam
\ Checked by: Ha Nguyen
\ Date: 2026-01-21

L = 6 "Span (m)"
...
```

### Add Sections

Use quote lines to organize:

```calcpad
"Main Report"

"Section 1: Input Data"
L = 6
h = 0.5

"Section 2: Calculations"
Area = L * h

"Section 3: Results"
Area = ? "Result"
```

---

## 📊 View Report Statistics

### Count Total Reports

```bash
ls cpdinput/*.cpd | wc -l   # Total CPD files
ls cpdoutput/*.html | wc -l # Total HTML files
ls cpdpdf/*.pdf | wc -l     # Total PDF files
```

### Check File Sizes

```bash
du -sh cpdoutput/           # Total HTML size
du -sh cpdpdf/              # Total PDF size
du -sh .                    # Total repo size
```

### List All Reports with Sizes

```bash
ls -lh cpdoutput/ | grep html | awk '{print $9, $5}'
```

---

## 🚀 Advanced: Local Testing

### Test Report Locally

```bash
# Install Calcpad locally
dotnet tool install --global Calcpad.Cli --version 7.5.9

# Run on your file
calcpad cpdinput/myfile.cpd

# View generated HTML
open cpdoutput/myfile.html    # macOS
xdg-open cpdoutput/myfile.html # Linux
start cpdoutput/myfile.html   # Windows
```

### Generate PDF Locally

```bash
# Convert HTML to PDF
wkhtmltopdf cpdoutput/myfile.html cpdpdf/myfile.pdf

# View the PDF
open cpdpdf/myfile.pdf        # macOS
xdg-open cpdpdf/myfile.pdf    # Linux
start cpdpdf/myfile.pdf       # Windows
```

### Test Index Generation

```bash
# Regenerate index
python3 scripts/update_index.py

# View generated HTML
open calcpad.html             # macOS
xdg-open calcpad.html         # Linux
start calcpad.html            # Windows
```

---

## 📚 Useful Resources

### Calcpad Documentation
- Official: https://www.calcpad.eu/
- Syntax Guide: https://www.calcpad.eu/en/documentation/
- Examples: https://www.calcpad.eu/en/examples/

### Git Cheat Sheet
```bash
# Basic commands
git add <file>              # Stage file
git commit -m "message"     # Commit with message
git push origin main        # Push to GitHub
git pull origin main        # Pull from GitHub
git status                  # Check status

# View history
git log --oneline          # Recent commits
git log <file>             # Commits for file
git show <commit>          # View commit details

# Undo changes
git restore <file>         # Discard local changes
git reset HEAD <file>      # Unstage file
git revert <commit>        # Undo commit (create new)
```

### Useful Commands

```bash
# Check everything is up to date
git status

# See what changed
git diff

# See full commit history
git log --oneline --all

# Check branch info
git branch -a

# See remote info
git remote -v
```

---

## ✅ Checklist Before Publishing

Before pushing a new report:

- ✅ File is in `cpdinput/` folder
- ✅ File has `.cpd` extension
- ✅ Report title is descriptive
- ✅ Calculations are correct
- ✅ No syntax errors in CPD file
- ✅ Descriptive commit message
- ✅ Pushed to origin/main

After pushing:

- ✅ Check GitHub Actions passed
- ✅ HTML generated in `cpdoutput/`
- ✅ PDF generated in `cpdpdf/`
- ✅ Report appears in `calcpad.html`
- ✅ Both links work
- ✅ Content looks correct

---

## 🆘 Need Help?

### Check Documentation

1. **README.md** - Overview and features
2. **PDF_GENERATION.md** - PDF-specific info
3. **This file** - Getting started guide

### Review Existing Reports

Look at CPD files in `cpdinput/` for examples:

```bash
cat cpdinput/test_workflow.cpd    # Simple example
cat cpdinput/biaxial_column.cpd   # Complex example
```

### Check Workflow Logs

Detailed error messages available at:
https://github.com/hydrostructai/calcpad_engineering/actions

Click latest run → Expand failed step for error details.

---

## 🎯 Next Steps

1. ✅ **You're set up!** Try adding your first report
2. 🔄 **Share with team** - Send them the GitHub link
3. 📚 **Learn Calcpad** - Read official documentation
4. 🎨 **Customize styling** - Edit CSS in HTML template
5. 🚀 **Integrate further** - Connect to external tools

---

**Last Updated:** 2026-01-21
