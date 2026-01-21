# Calcpad Engineering Reports

Automated structural engineering analysis and report generation using Calcpad with GitHub Actions CI/CD, dual HTML/PDF outputs, and custom domain hosting.

**Website:** https://hydrostructai.com  

---

## 📋 Quick Navigation

- [Quick Start](#-quick-start) - Get started in 30 seconds
- [Repository Structure](#-repository-structure) - Folder organization
- [How It Works](#-how-it-works) - The automation pipeline
- [Adding New Reports](#-adding-new-reports) - Create a new analysis
- [Documentation](#-documentation) - Learn more
- [Troubleshooting](#-troubleshooting) - Common issues

---

## 🚀 Quick Start

### View Existing Reports
1. Visit: **https://hydrostructai.com/calcpad_engineering/calcpad.html**
2. Click "📄 HTML" to view interactive report
3. Click "📕 PDF" to download printable version

### Add New Report (3 Steps)
```bash
# 1. Create or copy .cpd file
cp myanalysis.cpd calcpad_engineering/cpdinput/

# 2. Push to GitHub
cd calcpad_engineering
git add cpdinput/myanalysis.cpd
git commit -m "Add myanalysis"
git push origin main

# 3. Wait 1-2 minutes
# → HTML generated automatically
# → PDF generated automatically  
# → Index updated automatically
```

Then visit: https://hydrostructai.com/calcpad_engineering/calcpad.html

---

## 📁 Repository Structure

```
calcpad_engineering/
│
├── cpdinput/                        # Input: Raw .cpd source files
│   ├── test_workflow.cpd
│   ├── biaxial_column.cpd
│   └── [your .cpd files here]
│
├── cpdoutput/                       # Output: Generated HTML reports (interactive)
│   ├── test_workflow.html
│   ├── biaxial_column.html
│   └── [auto-generated]
│
├── cpdpdf/                          # Output: Generated PDF reports (printable)
│   ├── test_workflow.pdf
│   ├── biaxial_column.pdf
│   └── [auto-generated]
│
├── scripts/
│   └── update_index.py              # Python script: generates calcpad.html index
│
├── .github/workflows/
│   └── main.yml                     # GitHub Actions: automation workflow
│
├── calcpad.html                     # Main index page with report links
├── README.md                        # Calcpad guide
├── Guide-setup-run-calcpad.md       # Setup and automation guide
├── PDF_GENERATION.md                # PDF feature documentation
├── .gitignore                       # Git ignore patterns
└── LICENSE                          # MIT License
```

---

## ⚙️ How It Works

### The Automation Pipeline

```
You push .cpd file to GitHub
         ↓
GitHub Actions Detects Change (triggers on cpdinput/*.cpd)
         ↓
Step 1: Install & Run Calcpad
        $ calcpad cpdinput/file.cpd
        → Generates: cpdinput/file.html
         ↓
Step 2: Move HTML to Output
        $ mv cpdinput/file.html cpdoutput/file.html
         ↓
Step 3: Convert to PDF
        $ wkhtmltopdf cpdoutput/file.html cpdpdf/file.pdf
         ↓
Step 4: Update Index
        $ python3 scripts/update_index.py
        → Generates: calcpad.html with all links
         ↓
Step 5: Auto-Commit & Push
        $ git add cpdoutput/*.html cpdpdf/*.pdf calcpad.html
        $ git commit -m "Auto-generate reports"
        $ git push origin main
         ↓
GitHub Pages Deployed
         ↓
✨ Reports Live At:
   https://hydrostructai.com/calcpad_engineering/calcpad.html
```

### What Gets Generated

For each `.cpd` file pushed:

| Output | Location | Format | Use Case |
|--------|----------|--------|----------|
| **HTML** | `cpdoutput/file.html` | Interactive web page | View in browser, embed in docs |
| **PDF** | `cpdpdf/file.pdf` | Static document | Print, share, archive |
| **Index** | `calcpad.html` | Landing page | Navigation hub for all reports |

---

## ✨ Key Features

### ✅ Automated Workflow
- Push `.cpd` → Calcpad processes automatically
- No manual build steps needed
- GitHub Actions handles everything
- Completes in ~2 minutes

### ✅ Dual Format Output
- **HTML:** Interactive plots, responsive design, lightweight
- **PDF:** Print-optimized, downloadable, offline-compatible

### ✅ Smart Index
- Auto-generated from report metadata
- Shows both HTML and PDF links
- Displays file sizes
- Updates instantly on new reports

### ✅ GitHub Pages Hosting
- Free static hosting
- Custom domain support (hydrostructai.com)
- HTTPS enabled automatically
- Automatic updates on push

### ✅ Version Control
- All reports tracked in Git
- Complete history preserved
- Easy rollback
- Collaborative editing

---

## ➕ Adding New Reports

### Step 1: Create Your Analysis

Create a `.cpd` file using Calcpad Editor or text editor:

```calcpad
"Beam Analysis Report"
L = 6 "Span (m)"
P = 50 "Load (kN)"
I = 0.005 "Inertia (m⁴)"
M = P * L / 4
M = ? "Moment (kNm)"
```

### Step 2: Save & Push

```bash
# Copy to input folder
cp myanalysis.cpd /path/to/calcpad_engineering/cpdinput/

# Navigate to repo
cd /path/to/calcpad_engineering

# Push to GitHub
git add cpdinput/myanalysis.cpd
git commit -m "Add myanalysis: Description here"
git push origin main
```

### Step 3: Wait & Verify

1. **Wait 1-2 minutes** for GitHub Actions to process
2. **Check status:** https://github.com/hydrostructai/calcpad_engineering/actions
3. **View results:** https://hydrostructai.com/calcpad_engineering/calcpad.html

Your report should appear with both:
- 📄 HTML link (interactive)
- 📕 PDF link (downloadable)

---

## 🔄 GitHub Actions Workflow

### Files & Permissions

**Workflow File:** `.github/workflows/main.yml`

```yaml
# Trigger: When .cpd files are pushed
on:
  push:
    paths:
      - 'cpdinput/*.cpd'

# Permissions: Allow bot to commit
permissions:
  contents: write

# Runner: Ubuntu latest with pre-installed tools
jobs:
  process-calcpad:
    runs-on: ubuntu-latest
    steps:
      # ... runs Calcpad, generates HTML/PDF, updates index
```

### View Workflow Execution

1. Go to: https://github.com/hydrostructai/calcpad_engineering/actions
2. Click the latest workflow run
3. Review logs for each step
4. Check for errors or warnings

---

## 🔧 Troubleshooting

### ❓ Workflow Not Running
**Problem:** Pushed .cpd file but nothing happened

**Solution:**
1. Go to: https://github.com/hydrostructai/calcpad_engineering/actions
2. Check if workflow appears in list
3. Click workflow to see logs
4. Verify `.cpd` file is in `cpdinput/` folder
5. Check that workflow file exists: `.github/workflows/main.yml`

### ❓ HTML Exists But PDF Missing
**Problem:** Can see HTML report but no PDF link

**Solution:**
1. Check workflow logs for errors
2. Try locally: `wkhtmltopdf test.html test.pdf`
3. Verify repository has "Contents: Write" permission
4. Check PDF file exists: `ls -la cpdpdf/`

### ❓ Index Not Updated
**Problem:** Report file exists but doesn't show in calcpad.html

**Solution:**
1. Manually regenerate: `python3 scripts/update_index.py`
2. Verify HTML file exists: `ls -la cpdoutput/`
3. Run locally first to test
4. Commit and push updated `calcpad.html`

### ❓ Custom Domain Not Working
**Problem:** hydrostructai.com doesn't show reports

**Solution:**
1. Check DNS A records point to: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
2. Verify CNAME file exists: `cat CNAME`
3. Clear browser cache and try again
4. Wait 5 minutes for DNS propagation

---

## 📚 Documentation

### Included Files

- **README.md**
  - Calcpad introduction and quick setup guide
  - Simple .cpd file examples
  - Basic Calcpad concepts

- **Guide-setup-run-calcpad.md** (this file)
  - Complete setup and automation guide
  - Repository structure
  - GitHub Actions workflow details
  - Advanced troubleshooting

- **PDF_GENERATION.md**
  - How PDF generation works
  - Customizing PDF options
  - PDF-specific troubleshooting
  - Storage considerations

- **.github/workflows/main.yml**
  - Complete workflow code
  - Detailed step comments
  - Permission configuration

- **scripts/update_index.py**
  - Index generation logic
  - Metadata extraction
  - PDF detection

---

## 📊 Current Reports

All reports available at: **https://hydrostructai.com/calcpad_engineering/calcpad.html**

### Quick Stats
- **Total Reports:** 6
- **Format:** All have both HTML + PDF
- **Storage:** ~2.5 MB total
- **Hosting:** GitHub Pages (free)
- **Domain:** hydrostructai.com

### Report List
1. Test Workflow - Reference test case
2. Biaxial Column - Reinforced concrete analysis with Mander model
3. Biaxial Column Optimized - Optimized design variant
4. Flat Slab FEA - Finite element analysis
5. Flat Slab FEA Optimized - FEA optimization
6. Concrete Sections - Standard section reference

View with file sizes and download links at calcpad.html

---

## 🛠️ Local Development

### Prerequisites
- Python 3.7+
- Git
- Optional: Calcpad 7.5.9 (for local testing)
- Optional: wkhtmltopdf (for local PDF generation)

### Local Setup

```bash
# Clone repository
git clone https://github.com/hydrostructai/calcpad_engineering.git
cd calcpad_engineering

# Optional: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Generate reports locally
python3 scripts/update_index.py

# Test locally
python3 -m http.server 8000
# Then open: http://localhost:8000/calcpad.html
```

### Running Calcpad Locally

```bash
# Install Calcpad CLI
dotnet tool install --global Calcpad.Cli --version 7.5.9

# Run on single file
calcpad cpdinput/myfile.cpd

# Convert to PDF
wkhtmltopdf cpdoutput/myfile.html cpdpdf/myfile.pdf

# Regenerate index
python3 scripts/update_index.py
```

---

## 🔗 Quick Links

| Link | Purpose |
|------|---------|
| https://hydrostructai.com | Main website |
| https://hydrostructai.com/calcpad_engineering/calcpad.html | All reports |
| https://github.com/hydrostructai/calcpad_engineering | Source code |
| https://github.com/hydrostructai/calcpad_engineering/actions | Workflow status |
| https://www.calcpad.eu | Calcpad official |

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 👤 Contact

**Developer:** Ha Nguyen  
**Email:** ha.nguyen.cttl@gmail.com  
**GitHub:** [@Haah82](https://github.com/Haah82)

---

## ✅ Status

- ✅ GitHub Actions: Active
- ✅ Custom Domain: Active (hydrostructai.com)
- ✅ PDF Generation: Active
- ✅ Auto-Index: Active
- ✅ GitHub Pages: Live

---

**Last Updated:** 2026-01-22
