import os

def migrate_template(content):
    original_content = content
    # Ordem importa: casos específicos primeiro
    content = content.replace("ano: {{date}}", 'ano: <% tp.date.now("YYYY") %>')
    content = content.replace("{{date}}", '<% tp.date.now("YYYY-MM-DD") %>')
    content = content.replace("{{title}}", '<% tp.file.title %>')
    content = content.replace("{{time}}", '<% tp.date.now("HH:mm") %>')
    
    return content, content != original_content

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    print(f"Varrendo pasta: {folder_path}")
    
    count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".md") and filename != "migrate_templates.py":
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, changed = migrate_template(content)
            
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Migrado: {filename}")
                count += 1
                
    print(f"Total de arquivos migrados: {count}")

if __name__ == "__main__":
    main()
