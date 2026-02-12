#!/bin/bash

# Configuration
EXPORT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/obsidian-export"
REPO_DIR="$HOME/code/mission-control-obsidian"
MAIN_NOTE="mission-control-sistema-multi-agente-com-openclaw-(pt-br).html"

# Navigate to repo
cd "$REPO_DIR" || exit

# 1. Clean old files to ensure sync (optional but safer)
# git rm -rf ./* 2> /dev/null

# 2. Copy ALL exported files EXACTLY as they are
echo "📂 Copiando arquivos de exportação (modo fiel)..."
cp -R "$EXPORT_DIR/"* .

# 3. Create a clean redirect entry point (Does not touch the original files)
echo "🚪 Criando redirecionamento inicial (index.html)..."
cat > index.html <<EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; url='$MAIN_NOTE'">
    <script>window.location.href = "$MAIN_NOTE"</script>
</head>
<body>
    <p>Redirecionando para <a href="$MAIN_NOTE">o conteúdo principal</a>...</p>
</body>
</html>
EOF

# 4. Git Operations
echo "📦 Commitando mudanças..."
git add .
git commit -m "Deploy: Sincronização limpa (Vault Original) $(date '+%Y-%m-%d %H:%M:%S')"

echo "🚀 Enviando para o GitHub..."
git push origin main

echo "✅ Deploy Finalizado!"
