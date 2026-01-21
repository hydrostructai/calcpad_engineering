# Documentation Index

Complete guide to all documentation files in the Calcpad Engineering repository.

---

## 📖 Documentation Files

### 1. **README.md** - Main Project Documentation
**Purpose:** Project overview, features, setup, and troubleshooting  
**Audience:** All users  
**Length:** ~390 lines  
**Key Topics:**
- Quick start (30 seconds)
- Repository structure explanation
- How the automation pipeline works
- Key features overview
- Adding new reports (step-by-step)
- GitHub Actions workflow details
- Basic troubleshooting guide
- Local development setup
- External resources

**When to Read:** Start here for general understanding

---

### 2. **GETTING_STARTED.md** - New User Quick Guide
**Purpose:** Hands-on guide for adding first report  
**Audience:** New team members  
**Length:** ~475 lines  
**Key Topics:**
- First-time setup (5 minutes)
- Git configuration
- Adding first report (2 minutes)
- Checking report status
- Editing existing reports
- Common issues & solutions
- Customization examples
- Local testing procedures
- Useful Git commands
- Pre-publication checklist

**When to Read:** When adding your first report

---

### 3. **PDF_GENERATION.md** - PDF Feature Documentation
**Purpose:** Detailed PDF generation guide  
**Audience:** Users working with PDF output  
**Length:** ~370 lines  
**Key Topics:**
- PDF feature overview
- Automatic PDF generation process
- Dual format support (HTML + PDF)
- Smart index functionality
- PDF workflow steps
- Folder structure
- File size considerations
- Git repository impact
- Using PDF files
- Customizing PDF options
- PDF storage considerations
- Troubleshooting PDF issues
- GitHub Pages deployment
- Workflow permissions

**When to Read:** When using or customizing PDF output

---

### 4. **SYSTEM_SUMMARY.md** - Architecture & Status Overview
**Purpose:** Technical overview of system architecture and current status  
**Audience:** Technical leads, architects  
**Length:** ~389 lines  
**Key Topics:**
- Current repository status
- Repository statistics (files, sizes)
- System architecture diagram
- Documentation files created
- Features implemented
- Configuration details
- Next actions for completion
- How to complete system
- Final statistics
- Success criteria
- Quick links
- Checklist

**When to Read:** When understanding overall system architecture

---

### 5. **CODE FILES** - Configuration & Automation

#### .github/workflows/main.yml
**Purpose:** GitHub Actions automation workflow  
**Type:** YAML configuration  
**Key Features:**
- Triggered on `.cpd` file changes
- Installs Calcpad and dependencies
- Runs HTML generation
- Converts HTML to PDF
- Updates index
- Auto-commits results
- Permissions for bot access

#### scripts/update_index.py
**Purpose:** Generate index from report files  
**Type:** Python script  
**Key Features:**
- Scans `cpdoutput/` for HTML
- Scans `cpdpdf/` for PDF
- Extracts metadata from HTML
- Creates `calcpad.html` index
- Shows file sizes
- Conditional PDF linking

#### .gitignore
**Purpose:** Exclude auto-generated files  
**Type:** Git configuration  
**Contents:**
- Auto-generated HTML/PDF
- Python cache files
- Build outputs
- System files

---

## 🗂️ File Organization

```
calcpad_engineering/
│
├── Documentation Files (READ FIRST)
│   ├── README.md ..................... Main overview
│   ├── GETTING_STARTED.md ........... Quick start guide
│   ├── PDF_GENERATION.md ........... PDF feature guide
│   ├── SYSTEM_SUMMARY.md ........... Architecture overview
│   └── DOCUMENTATION_INDEX.md ...... This file
│
├── Configuration Files
│   ├── .github/workflows/main.yml ... GitHub Actions
│   ├── .gitignore ................... Git ignore patterns
│   └── scripts/
│       └── update_index.py ........ Index generation
│
├── Input Files
│   └── cpdinput/*.cpd .............. Source analysis files
│
├── Generated Output
│   ├── cpdoutput/*.html ........... Interactive reports
│   ├── cpdpdf/*.pdf ............... Printable reports
│   └── calcpad.html ............... Report index
│
└── Other
    └── LICENSE ..................... MIT License
```

---

## 🎯 Reading Guide by Use Case

### "I'm new and want to understand the project"
**Read in this order:**
1. [README.md](README.md) - Overview
2. [SYSTEM_SUMMARY.md](SYSTEM_SUMMARY.md) - Architecture
3. [GETTING_STARTED.md](GETTING_STARTED.md) - Hands-on

### "I want to add my first report"
**Read:**
1. [GETTING_STARTED.md](GETTING_STARTED.md) - Complete guide
2. [README.md](README.md#-adding-new-reports) - Adding reports section

### "I need to work with PDF output"
**Read:**
1. [PDF_GENERATION.md](PDF_GENERATION.md) - Full details
2. [README.md](README.md#-features) - Feature overview

### "I'm troubleshooting an issue"
**Read:**
1. [README.md](README.md#-troubleshooting) - Common issues
2. [GETTING_STARTED.md](GETTING_STARTED.md#-common-issues) - More examples
3. [PDF_GENERATION.md](PDF_GENERATION.md#troubleshooting) - PDF issues

### "I'm setting up or configuring the system"
**Read:**
1. [SYSTEM_SUMMARY.md](SYSTEM_SUMMARY.md) - Configuration details
2. [README.md](README.md#-github-actions-workflow) - Workflow details
3. [PDF_GENERATION.md](PDF_GENERATION.md#configuration-files) - PDF config

---

## 📊 Documentation Statistics

| Document | Lines | Type | Focus |
|----------|-------|------|-------|
| README.md | ~390 | Overview | Features & quick start |
| GETTING_STARTED.md | ~475 | Guide | Step-by-step instructions |
| PDF_GENERATION.md | ~370 | Reference | PDF feature details |
| SYSTEM_SUMMARY.md | ~389 | Technical | Architecture & status |
| Code Comments | 200+ | Code | Inline documentation |
| **TOTAL** | **1,200+** | Mixed | Comprehensive |

---

## 🔗 External References

### Calcpad
- Official Website: https://www.calcpad.eu/
- Documentation: https://www.calcpad.eu/en/documentation/
- CLI Tool: https://www.calcpad.eu/en/download/

### GitHub
- GitHub Pages: https://pages.github.com/
- Actions: https://github.com/features/actions
- Documentation: https://docs.github.com/

### Tools
- wkhtmltopdf: https://wkhtmltopdf.org/
- Three.js: https://threejs.org/
- Plotly.js: https://plotly.com/javascript/

---

## 🔍 Search Guide

### By Topic

**Automation & Workflow:**
- See: [README.md - How It Works](README.md#-how-it-works)
- See: [SYSTEM_SUMMARY.md - Architecture](SYSTEM_SUMMARY.md#-system-architecture)

**Adding Reports:**
- See: [README.md - Adding New Reports](README.md#-adding-new-reports)
- See: [GETTING_STARTED.md - Add First Report](GETTING_STARTED.md#-add-your-first-report-2-minutes)

**PDF Features:**
- See: [PDF_GENERATION.md](PDF_GENERATION.md)
- See: [README.md - Features](README.md#-key-features)

**Troubleshooting:**
- See: [README.md - Troubleshooting](README.md#-troubleshooting)
- See: [GETTING_STARTED.md - Common Issues](GETTING_STARTED.md#-common-issues)

**Technical Details:**
- See: [SYSTEM_SUMMARY.md - Configuration](SYSTEM_SUMMARY.md#-configuration-details)
- See: [PDF_GENERATION.md - How It Works](PDF_GENERATION.md#how-it-works)

**GitHub & Git:**
- See: [README.md - GitHub Actions Workflow](README.md#-github-actions-workflow)
- See: [GETTING_STARTED.md - Useful Commands](GETTING_STARTED.md#-useful-resources)

---

## ✅ Documentation Checklist

**What's Covered:**
- ✅ Project overview and features
- ✅ Quick start guide (5-30 minutes)
- ✅ Step-by-step tutorials
- ✅ How the automation works
- ✅ PDF generation details
- ✅ Troubleshooting common issues
- ✅ Configuration instructions
- ✅ Local development setup
- ✅ External resources
- ✅ Architecture overview

**What's Included:**
- ✅ 1,200+ lines of documentation
- ✅ Multiple formats (overview, guides, reference)
- ✅ Code examples and commands
- ✅ Diagrams and visuals
- ✅ Tables and structured data
- ✅ Checklists and guides

---

## 🚀 Getting Started

**New to the project?**

1. Start: [README.md](README.md) (5 min read)
2. Learn: [SYSTEM_SUMMARY.md](SYSTEM_SUMMARY.md) (10 min read)
3. Do: [GETTING_STARTED.md](GETTING_STARTED.md) (follow steps)

**Questions?**

1. Search this index for your topic
2. Check the relevant documentation
3. Review the troubleshooting section

---

## 📞 Support

For help:
1. Check the relevant documentation file
2. Review troubleshooting sections
3. Check GitHub Actions logs
4. Review example CPD files
5. Consult Calcpad documentation

---

## 🔄 Documentation Updates

**Last Updated:** 2026-01-21  
**Status:** Complete and current  
**Version:** 1.0

---

**Navigation:** [Back to README](README.md) | [GitHub](https://github.com/hydrostructai/calcpad_engineering) | [Website](https://hydrostructai.com)
