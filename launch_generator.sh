#!/bin/bash
# Pentest Engagement Generator Launcher

echo ""
echo "=========================================="
echo "   Pentest Engagement Generator"
echo "=========================================="
echo ""

if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "[INFO] Starting Engagement Generator..."
python3 "$(dirname "$0")/scripts/engagement_generator.py"
