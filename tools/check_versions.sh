#!/bin/bash
# Script to check BOM dependency versions
# Usage: check_versions.sh

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Move to project root directory (parent of tools folder)
cd "$SCRIPT_DIR/.."

# Execute Python script
python "$SCRIPT_DIR/check_versions.py" "$@"
