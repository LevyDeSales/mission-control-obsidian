# Mission Control Obsidian

Este repositório armazena o site estático gerado a partir de notas do Obsidian, publicado automaticamente via GitHub Pages.

🔗 **Acesse o site:** [https://levydesales.github.io/mission-control-obsidian/](https://levydesales.github.io/mission-control-obsidian/)

---

## 🚀 Como Atualizar o Site

O processo foi simplificado para 2 passos: **Exportar** e **Publicar**.

### 1. No Obsidian (Exportar)
Use o plugin **Webpage HTML Export**.

1.  Faça suas edições no Obsidian.
2.  Abra a Command Palette (`Cmd + P`) e rode: `Webpage HTML Export: Export to HTML`.
3.  Confirme a exportação (certifique-se de que está salvando na pasta `obsidian-export` do seu iCloud Drive).

> **Nota:** O sistema espera que a nota principal se chame `Mission Control - Sistema Multi-Agente com OpenClaw (PT-BR)`. Ela será transformada automaticamente na página inicial (`index.html`).

### 2. No Terminal (Publicar)
Abra seu terminal e rode o script de automação:

```bash
~/code/mission-control-obsidian/publish.sh
```

**O que o script faz?**
1.  Copia os arquivos recém-exportados do iCloud para o repositório.
2.  Renomeia a nota principal para `index.html`.
3.  Envia tudo para o GitHub.
4.  O GitHub Pages atualiza o site em 1-2 minutos.

---

## ➕ Adicionando Outras Páginas
Se você quiser publicar outras notas além da principal:

1.  Exporte-as junto com a principal (ou para a mesma pasta `obsidian-export`).
2.  Rode o script `publish.sh`.
3.  As novas páginas estarão acessíveis pelo nome do arquivo.
    *   Exemplo: Se exportar `Minha Nota.md`, ela vira `minha-nota.html` e você acessa em:
        `.../mission-control-obsidian/minha-nota.html`

## 📂 Estrutura
- **Local do Repo:** `~/code/mission-control-obsidian`
- **Pasta de Origem (Export):** `~/Library/Mobile Documents/com~apple~CloudDocs/obsidian-export`
- **Script:** `publish.sh`
