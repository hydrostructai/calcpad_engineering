.PHONY: build test trigger help

help:
	@echo "📋 Calcpad Engineering Makefile"
	@echo "Available commands:"
	@echo "  make build       - Generate reports locally"
	@echo "  make test        - Test Calcpad installation"
	@echo "  make trigger     - Trigger GitHub Action by updating .cpd"
	@echo "  make clean       - Remove generated HTML files"

test:
	@echo "🔍 Testing Calcpad installation..."
	which calcpad && calcpad --version || echo "⚠️  Calcpad not found"

build:
	@echo "🔨 Building reports locally..."
	@mkdir -p cpdoutput
	@for file in cpdinput/*.cpd; do \
		[ -e "$$file" ] || continue; \
		filename=$$(basename "$$file" .cpd); \
		echo "📄 Processing: $$filename"; \
		calcpad "$$file"; \
		if [ -f "cpdinput/$$filename.html" ]; then \
			mv "cpdinput/$$filename.html" "cpdoutput/$$filename.html"; \
			echo "✅ Generated: cpdoutput/$$filename.html"; \
		fi \
	done
	@echo "📊 Updating index..."
	@python3 scripts/update_index.py
	@echo "✨ Done!"

clean:
	@echo "🧹 Cleaning up..."
	@rm -rf cpdoutput/*.html
	@echo "✅ Cleaned!"

trigger:
	@echo "🚀 Triggering GitHub Action..."
	@echo "Touching cpdinput files to force push..."
	@touch cpdinput/*.cpd
	@git add cpdinput/*.cpd
	@git commit -m "Trigger workflow [skip ci]" || echo "No changes"
	@git push
	@echo "✅ Workflow triggered! Check Actions tab on GitHub."
