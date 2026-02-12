#!/bin/bash

# Configuration
EXPORT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/obsidian-export"
REPO_DIR="$HOME/code/mission-control-obsidian"

# Define filenames (Original names from Obsidian export)
PT_BR_NOTE="mission-control-sistema-multi-agente-com-openclaw-(pt-br).html"
EN_NOTE="mission-control-sistema-multi-agente-com-openclaw.html"

# Navigate to repo
cd "$REPO_DIR" || exit

# 1. Copy ALL exported files (includes both HTMLs, assets, site-lib)
echo "📂 Copiando arquivos de exportação..."
cp -R "$EXPORT_DIR/"* .

# 2. Setup Homepage (PT-BR -> index.html)
if [ -f "$PT_BR_NOTE" ]; then
    echo "🔄 Transformando Nota PT-BR em Home (index.html)..."
    
    # Rename file
    mv "$PT_BR_NOTE" index.html
    
    # 2.1 Patch Metadata in index.html (Fixes Graph connection)
    echo "🔧 Ajustando metadados da página..."
    # Update pathname and og:url to identify as index.html
    sed -i '' "s/name=\"pathname\" content=\"$PT_BR_NOTE\"/name=\"pathname\" content=\"index.html\"/g" index.html
    sed -i '' "s/property=\"og:url\" content=\"$PT_BR_NOTE\"/property=\"og:url\" content=\"index.html\"/g" index.html
    
    # 2.2 Patch Sidebar Menu (file-tree-content.html) (Fixes Active State & Navigation)
    TREE_FILE="site-lib/html/file-tree-content.html"
    if [ -f "$TREE_FILE" ]; then
        echo "🌲 Atualizando menu lateral..."
        # Replace the href link
        sed -i '' "s/href=\"$PT_BR_NOTE\"/href=\"index.html\"/g" "$TREE_FILE"
        # Optional: Add 'active' class logic if needed, but href match usually suffices for the JS
    else
        echo "⚠️ Menu lateral não encontrado em $TREE_FILE"
    fi
    
else
    echo "⚠️ AVISO: Nota PT-BR original ($PT_BR_NOTE) não encontrada. Verifique se exportou com o nome correto."
fi

# 3. Git Operations
echo "📦 Commitando mudanças..."
git add .
git commit -m "Build: Deploy automatizado com correção de Index/Menu $(date '+%Y-%m-%d %H:%M:%S')"

echo "🚀 Enviando para o GitHub..."
git push origin main

echo "✅ Deploy Finalizado!"
