#!/bin/bash
# This script cleans up the project directory by removing all __pycache__ directories. 
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name ".mypy_cache" -exec rm -rf {} +