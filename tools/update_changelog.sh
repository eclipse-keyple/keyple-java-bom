#!/bin/bash
# Script to update CHANGELOG.md
# Usage: update_changelog.sh [YYYY.MM.DD]

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Move to project root directory (parent of tools folder)
cd "$SCRIPT_DIR/.."

# Execute Python script
python "$SCRIPT_DIR/update_changelog.py" "$@"
