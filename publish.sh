#!/bin/bash

# Configuration
EXPORT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/obsidian-export"
REPO_DIR="$HOME/code/mission-control-obsidian"

# Define filenames
PT_BR_NOTE="mission-control-sistema-multi-agente-com-openclaw-(pt-br).html"
EN_NOTE="mission-control-sistema-multi-agente-com-openclaw.html"

# Navigate to repo
cd "$REPO_DIR" || exit

# Copy ALL exported files (includes both HTMLs and assets)
echo "📂 Copiando arquivos de exportação..."
cp -R "$EXPORT_DIR/"* .

# Setup Homepage (PT-BR -> index.html)
if [ -f "$PT_BR_NOTE" ]; then
    echo "🔄 Configurando Home (PT-BR)..."
    cp "$PT_BR_NOTE" index.html
    
    # Patch metadata for index.html (fixes Graph/TOC on Home)
    echo "🔧 Ajustando metadados da Home..."
    sed -i '' "s/name=\"pathname\" content=\"$PT_BR_NOTE\"/name=\"pathname\" content=\"index.html\"/g" index.html
    sed -i '' "s/property=\"og:url\" content=\"$PT_BR_NOTE\"/property=\"og:url\" content=\"index.html\"/g" index.html
    
    # Remove the original PT-BR file to avoid duplication in the repo (optional, but cleaner)
    # rm "$PT_BR_NOTE" 
else
    echo "⚠️ AVISO: Nota PT-BR não encontrada: $PT_BR_NOTE"
fi

# Git operations
echo "📦 Commitando mudanças..."
git add .
git commit -m "Update: Publicação Dual-Lang $(date '+%Y-%m-%d %H:%M:%S')"

echo "🚀 Enviando para o GitHub..."
git push origin main

echo "✅ Feito!"
