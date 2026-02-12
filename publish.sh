#!/bin/bash

# Configuration
EXPORT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/obsidian-export"
REPO_DIR="$HOME/code/mission-control-obsidian"
MAIN_NOTE_NAME="mission-control-sistema-multi-agente-com-openclaw-(pt-br).html"

# Navigate to repo
cd "$REPO_DIR" || exit

# Copy files
echo "📂 Copiando arquivos de exportação..."
cp -R "$EXPORT_DIR/"* .

# Rename main entry point
if [ -f "$MAIN_NOTE_NAME" ]; then
    echo "🔄 Renomeando nota principal para index.html..."
    mv "$MAIN_NOTE_NAME" index.html
    
    # Fix the redirect loop issue by patching the metadata
    echo "🔧 Corrigindo metadados de redirecionamento..."
    sed -i '' "s/name=\"pathname\" content=\"$MAIN_NOTE_NAME\"/name=\"pathname\" content=\"index.html\"/g" index.html
    sed -i '' "s/property=\"og:url\" content=\"$MAIN_NOTE_NAME\"/property=\"og:url\" content=\"index.html\"/g" index.html
fi

# Git operations
echo "📦 Commitando mudanças..."
git add .
git commit -m "Update: $(date '+%Y-%m-%d %H:%M:%S')"

echo "🚀 Enviando para o GitHub..."
git push origin main

echo "✅ Feito!"
