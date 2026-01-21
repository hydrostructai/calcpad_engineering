#!/bin/bash

# Local processing script for Calcpad Engineering Reports
# Processes all .cpd files in cpdinput/ and generates HTML/PDF outputs

PROJECT_ROOT="/home/hha/work/github-guide/calcpad_engineering"
INPUT_DIR="$PROJECT_ROOT/cpdinput"
OUTPUT_DIR="$PROJECT_ROOT/cpdoutput"
PDF_DIR="$PROJECT_ROOT/cpdpdf"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"

# Ensure directories exist
mkdir -p "$OUTPUT_DIR" "$PDF_DIR"

echo "🚀 Starting local Calcpad processing..."
echo "----------------------------------------"

# Check dependencies
if ! command -v calcpad-run &> /dev/null; then
    echo "❌ Error: calcpad-run not found. Please install it first."
    exit 1
fi

# Loop through all .cpd files in input directory
for cpd_file in "$INPUT_DIR"/*.cpd; do
    [ -e "$cpd_file" ] || continue
    
    filename=$(basename "$cpd_file" .cpd)
    echo "📄 Processing: $filename.cpd"
    
    # Run calcpad
    cd "$PROJECT_ROOT"
    if calcpad-run "$cpd_file"; then
        HTML_NEW="$PROJECT_ROOT/$filename.html"
        HTML_OLD="$INPUT_DIR/$filename.html"
        TARGET_HTML="$OUTPUT_DIR/$filename.html"
        
        if [ -f "$HTML_NEW" ]; then
            mv "$HTML_NEW" "$TARGET_HTML"
        elif [ -f "$HTML_OLD" ]; then
            mv "$HTML_OLD" "$TARGET_HTML"
        fi
        
        if [ -f "$TARGET_HTML" ]; then
            echo "  ✅ HTML generated"
            
            # Fix broken local paths in HTML
            sed -i 's|https://calcpad.local/file:///||g' "$TARGET_HTML"
            sed -i 's|https://calcpad.local/||g' "$TARGET_HTML"
            
            # Generate PDF if wkhtmltopdf is available
            if command -v wkhtmltopdf &> /dev/null; then
                echo "  📝 Converting to PDF..."
                wkhtmltopdf --quiet --enable-local-file-access "$TARGET_HTML" "$PDF_DIR/$filename.pdf"
                if [ $? -eq 0 ]; then
                    echo "  ✅ PDF generated"
                else
                    echo "  ❌ PDF generation failed"
                fi
            fi
        else
            echo "  ⚠️  HTML file not found after run."
        fi
    else
        echo "  ❌ Calcpad execution failed for $filename.cpd"
    fi
    echo "----------------------------------------"
done

# Update the index page
echo "🔄 Updating calcpad.html index..."
python3 "$SCRIPTS_DIR/update_index.py"

echo "✨ All tasks completed!"
