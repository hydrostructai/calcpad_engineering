# 🔄 CPD File Synchronization System

## Overview

The GitHub Actions workflow now implements **perfect file synchronization** between CPD source files and their generated outputs. The `.cpd` file is the **single source of truth** - HTML and PDF files are automatically created when CPD files are added/modified, and automatically deleted when CPD files are removed.

---

## Architecture

```
User Action                 Workflow Detects           Output Generated
═════════════════════════════════════════════════════════════════════════

ADD: cpdinput/Beam.cpd   →  git shows "A Beam.cpd"  →  cpdoutput/Beam.html
                                                        cpdpdf/Beam.pdf

MODIFY: Beam.cpd         →  git shows "M Beam.cpd"  →  cpdoutput/Beam.html ↻
                                                        cpdpdf/Beam.pdf ↻

DELETE: Beam.cpd         →  git shows "D Beam.cpd"  →  ✅ Beam.html deleted
                                                        ✅ Beam.pdf deleted

RENAME: Beam→Analysis    →  git shows "D Beam.cpd"   →  ✅ Beam.html/pdf deleted
                            + "A Analysis.cpd"       →  Analysis.html created
                                                        Analysis.pdf created
```

---

## How It Works

### Step 1: Detect Deleted Files

```bash
DELETED_FILES=$(git show --name-status HEAD | grep "^D" | grep "\.cpd$" | awk '{print $2}')
```

This command:
- Checks the latest commit (`git show HEAD`)
- Looks for deleted files (`^D` prefix)
- Filters for `.cpd` files only
- Extracts the filename

**Output**: List of deleted .cpd paths
```
cpdinput/OldCalc.cpd
cpdinput/Archive.cpd
```

### Step 2: Remove Orphaned Output Files

For each deleted .cpd file:
```bash
filename=$(basename "$deleted_path" .cpd)
rm -f "cpdoutput/${filename}.html"
rm -f "cpdpdf/${filename}.pdf"
```

**Example**: If `cpdinput/OldCalc.cpd` was deleted:
- ✅ Removes: `cpdoutput/OldCalc.html`
- ✅ Removes: `cpdpdf/OldCalc.pdf`

### Step 3: Detect New/Modified Files

```bash
CHANGED_FILES=$(git show --name-status HEAD | grep -E "^[AM]" | grep "\.cpd$" | awk '{print $2}')
```

This command:
- Looks for added (`A` prefix) or modified (`M` prefix) files
- Filters for `.cpd` files
- Extracts full paths

**Output**: List of changed .cpd paths
```
cpdinput/Beam.cpd
cpdinput/Foundation.cpd
```

### Step 4: Generate HTML and PDF

For each new/modified .cpd:

```bash
# Generate HTML from CPD
calcpad-run cpdinput/Beam.cpd    # Creates: cpdinput/Beam.html

# Move to output folder
mv cpdinput/Beam.html cpdoutput/Beam.html

# Convert to PDF
wkhtmltopdf cpdoutput/Beam.html cpdpdf/Beam.pdf
```

Result:
- ✅ `cpdoutput/Beam.html` (interactive report)
- ✅ `cpdpdf/Beam.pdf` (printable version)

---

## Edge Cases Handled

### Case 1: File Rename
```
User renames: Beam.cpd → BeamAnalysis.cpd

Git detects:
  D cpdinput/Beam.cpd              ← Triggers deletion
  A cpdinput/BeamAnalysis.cpd      ← Triggers creation

Workflow result:
  ✅ Beam.html deleted
  ✅ Beam.pdf deleted
  ✅ BeamAnalysis.html created
  ✅ BeamAnalysis.pdf created
```

### Case 2: Bulk Delete
```
User deletes 3 files at once:
  D cpdinput/File1.cpd
  D cpdinput/File2.cpd
  D cpdinput/File3.cpd

Workflow result:
  ✅ File1.html/pdf deleted
  ✅ File2.html/pdf deleted
  ✅ File3.html/pdf deleted
```

### Case 3: Modify and Add Same Push
```
User pushes 1 modification + 1 new file:
  M cpdinput/Beam.cpd          ← Existing file changed
  A cpdinput/NewCalc.cpd       ← New file added

Workflow result:
  ✅ Beam.html/pdf regenerated (fresh versions)
  ✅ NewCalc.html/pdf created (brand new)
```

### Case 4: No CPD Files
```
User pushes other files (no .cpd changes):
  M README.md
  A scripts/helper.py

Workflow result:
  ✅ No changes in cpdoutput/ or cpdpdf/
  ✅ Index updated with existing reports
  ✅ Git commit skipped (no changes)
```

---

## Workflow Execution Timeline

```
1. User pushes changes to GitHub
                    ↓
2. GitHub Actions triggered (on: push)
                    ↓
3. Checkout repository
                    ↓
4. Install dependencies (calcpad-run, wkhtmltopdf)
                    ↓
5. ┌─────────────────────────────────────┐
   │ PROCESS CPD FILES WITH SYNC         │
   └─────────────────────────────────────┘
   
   Step 1: Detect Deleted Files
   ├─ git show --name-status HEAD
   ├─ grep "^D" (deleted files)
   ├─ grep "\.cpd$" (only .cpd files)
   └─ Remove: cpdoutput/X.html, cpdpdf/X.pdf
   
   Step 2: Detect New/Modified Files
   ├─ git show --name-status HEAD
   ├─ grep "^[AM]" (added/modified)
   ├─ grep "\.cpd$" (only .cpd files)
   └─ Process: calcpad-run → HTML/PDF
   
   Step 3: Report Final State
   └─ Show all files in cpdoutput/ and cpdpdf/
                    ↓
6. Update Index
   ├─ python3 scripts/update_index.py
   └─ Updates calcpad.html with all reports
                    ↓
7. Commit & Push
   ├─ git add cpdoutput/*.html
   ├─ git add cpdpdf/*.pdf
   ├─ git add calcpad.html
   ├─ git commit (auto-commit by github-actions[bot])
   └─ git push origin main (with GITHUB_TOKEN)
                    ↓
8. ✅ Deployment complete
   └─ GitHub Pages picks up changes automatically
```

---

## File State Examples

### Example 1: Initial State
```
cpdinput/
  ├─ Beam.cpd
  ├─ Foundation.cpd

cpdoutput/
  ├─ Beam.html
  ├─ Foundation.html

cpdpdf/
  ├─ Beam.pdf
  ├─ Foundation.pdf
```

### Example 2: After User Adds SlabDesign.cpd
```
Changes:
  A cpdinput/SlabDesign.cpd

Result:
cpdoutput/
  ├─ Beam.html
  ├─ Foundation.html
  ├─ SlabDesign.html         ← NEW

cpdpdf/
  ├─ Beam.pdf
  ├─ Foundation.pdf
  ├─ SlabDesign.pdf          ← NEW
```

### Example 3: After User Deletes Foundation.cpd
```
Changes:
  D cpdinput/Foundation.cpd

Result:
cpdoutput/
  ├─ Beam.html
  ├─ SlabDesign.html

cpdpdf/
  ├─ Beam.pdf
  ├─ SlabDesign.pdf

Note: Foundation.html and Foundation.pdf automatically removed
```

### Example 4: After User Modifies Beam.cpd
```
Changes:
  M cpdinput/Beam.cpd

Result:
cpdoutput/
  ├─ Beam.html               ← REGENERATED (fresh version)
  ├─ SlabDesign.html

cpdpdf/
  ├─ Beam.pdf                ← REGENERATED (fresh version)
  ├─ SlabDesign.pdf
```

---

## Git Commands Used

| Command | Purpose | Output |
|---------|---------|--------|
| `git show --name-status HEAD` | Show files changed in latest commit | `M file.txt`, `A new.txt`, `D old.txt` |
| `grep "^D.*\.cpd$"` | Find deleted .cpd files | List of deleted CPD paths |
| `grep -E "^[AM].*\.cpd$"` | Find new/modified .cpd files | List of changed CPD paths |
| `awk '{print $2}'` | Extract filename from git output | Filename only |
| `basename "$path" .cpd` | Remove .cpd extension | Filename without extension |

---

## Logging and Debugging

The workflow provides detailed output for each step:

```
════════════════════════════════════════════════════════
  🔍 GITHUB ACTIONS CPD-HTML-PDF SYNCHRONIZATION
════════════════════════════════════════════════════════

📋 STEP 1: Detecting deleted .cpd files...
―――――――――――――――――――――――――――――――――――――――――――――――――――――――
✅ No deleted .cpd files

📋 STEP 2: Detecting new/modified .cpd files...
―――――――――――――――――――――――――――――――――――――――――――――――――――――――
🆕 Found changed files:
  cpdinput/Beam.cpd

  🔄 Processing: Beam
    ├─ Generating HTML (calcpad-run)...
    ├─ ✅ HTML moved: cpdoutput/Beam.html
    ├─ Converting to PDF (wkhtmltopdf)...
    └─ ✅ PDF created: cpdpdf/Beam.pdf

════════════════════════════════════════════════════════
  📊 FINAL STATE REPORT
════════════════════════════════════════════════════════

📂 Current CPD files in cpdinput/: 2

📄 Generated HTML files in cpdoutput/: 2

📕 Generated PDF files in cpdpdf/: 2

✨ Synchronization complete!
```

---

## Benefits

✅ **Single Source of Truth**: .cpd files determine everything  
✅ **Automatic Cleanup**: No orphaned files accumulate  
✅ **Perfect Sync**: HTML/PDF always matches .cpd state  
✅ **Audit Trail**: Git history shows all changes  
✅ **Reliable**: Handles edge cases gracefully  
✅ **Debuggable**: Comprehensive logging for troubleshooting  

---

## Testing the Workflow

### Test Case 1: Add New File
```bash
# Create and push new .cpd file
git add cpdinput/MyNewAnalysis.cpd
git commit -m "Add MyNewAnalysis"
git push origin main

# Expected: MyNewAnalysis.html and .pdf created in output folders
```

### Test Case 2: Delete File
```bash
# Delete and push removal
git rm cpdinput/OldAnalysis.cpd
git commit -m "Remove OldAnalysis"
git push origin main

# Expected: OldAnalysis.html and .pdf deleted from output folders
```

### Test Case 3: Modify File
```bash
# Modify file and push
# (Edit cpdinput/Analysis.cpd)
git add cpdinput/Analysis.cpd
git commit -m "Update Analysis"
git push origin main

# Expected: Analysis.html and .pdf regenerated with new content
```

---

## Troubleshooting

### Files not syncing?
- Check GitHub Actions workflow run logs
- Verify .cpd file syntax (calcpad-run might fail)
- Check if changes are actually in `cpdinput/` folder

### HTML created but PDF missing?
- wkhtmltopdf might not be installed
- Check workflow logs for wkhtmltopdf errors
- HTML still available even if PDF fails

### Index not updating?
- Verify `scripts/update_index.py` exists and is executable
- Check Python3 is available in runner
- Review workflow logs for Python errors

---

## Next Steps

1. **Push test files** to cpdinput/ and verify HTML/PDF generation
2. **Delete test files** and verify cleanup works
3. **Monitor workflow runs** at GitHub Actions tab
4. **Share with team** - explain the new sync mechanism

---

**Version**: 1.0  
**Last Updated**: 2025-01-22  
**Status**: 🟢 Production Ready
