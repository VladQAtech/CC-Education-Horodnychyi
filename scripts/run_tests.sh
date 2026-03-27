#!/bin/bash
# Test automation script for Promova web tests

set -e  # зупинитись при помилці

echo "Running Promova web tests..."

# Запуск тестів з HTML звітом
pytest tests/web/ \
  --html=reports/report.html \
  --self-contained-html \
  -v

echo "Done! Report saved to reports/report.html"
# Trigger: testing Claude Code GitHub Actions workflow
