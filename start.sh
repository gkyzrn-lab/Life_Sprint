#!/bin/bash

# Life Sprint Game - Start Script
# This script starts the Life Sprint backend API server

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$PROJECT_DIR/.venv"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║           🎮 LIFE SPRINT - STARTING BACKEND 🎮              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if venv exists
if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Virtual environment not found at $VENV_PATH"
    echo "Please run: python3 -m venv .venv && pip install -r requirements.txt"
    exit 1
fi

# Activate venv
source "$VENV_PATH/bin/activate"

echo "✅ Virtual environment activated"
echo ""

# Check which port to use
PORT=${1:-8000}

# Check if port is available
if lsof -i :$PORT >/dev/null 2>&1; then
    echo "⚠️  Port $PORT is already in use"
    PORT=$((PORT + 1))
    echo "   Trying port $PORT instead..."
fi

echo "📡 Starting API server on http://127.0.0.1:$PORT"
echo ""
echo "Available endpoints:"
echo "  • http://127.0.0.1:$PORT/docs     (Interactive API docs)"
echo "  • http://127.0.0.1:$PORT/          (API status)"
echo ""
echo "Press CTRL+C to stop the server"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start the server
uvicorn main:app --host 127.0.0.1 --port $PORT
