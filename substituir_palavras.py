import os
import re

# ==========================================
# 1. CORREÇÕES DE ERROS ANTERIORES
# ==========================================
correcoes = {
    "imidade:": "image:",       # Restaurar chave de configuração quebrada
    "Imidades": "Imagens",      # Corrigir título quebrado
    "imidade": "imagem",        # Corrigir texto quebrado
    "usidade": "usage",         # Caso usage tenha virado usidade
    "pidade": "page",           # Caso page tenha virado pidade
    "manidade": "manage",       # Caso manage tenha virado manidade
    "Viidadens": "Viagens",     # Corrigir Viagens (Vi+age+ns)
    "Viidadem": "Viagem",       # Corrigir Viagem (Vi+age+m)
    "Postidadens": "Postagens", # Corrigir Postagens (Post+age+ns)
    "viidadens": "viagens",     # Corrigir variante minúscula
}

# ==========================================
# 2. SUBSTITUIÇÕES (PALAVRAS INTEIRAS - REGEX)
# Use para palavras que podem ser parte de outras (ex: age, food, Note)
# ==========================================
subst_palavras = {
    # Solicitados (Novos - Case Sensitive Explicito)
    "map": "mapa",
    "Map": "Mapa",
    "Conference": "Conferência",
    "conference": "conferência",
    "sessions": "sessões",
    "Sessions": "Sessões",
    "Speaker": "Palestrante",
    "Speakers": "Palestrantes",
    "Restaurants": "Restaurantes",
    "Movies": "Filmes",
    "movies": "filmes",
    "genres": "gêneros",
    "start": "início",
    "end": "fim",
    "events": "eventos",
    "season": "temporada",
    "episode": "episódio",
    "episodes": "episódios",
    "guests": "convidados",
    "Food": "Comida",
    "attribution": "atribuição",
    "coordinates": "coordenadas",
    "Trips": "Viagens",
    "trips": "viagens",
    
    # Anteriores (Mantidos e Refinados)
    "Note": "Nota",
    "note": "nota",
    "journal": "diário",
    "Journal": "Diário",
    "Diretors": "Diretores",
    "Directors": "Diretores",
    "Conferences": "Conferências",
    "food": "comida",
    "Quotes": "Citações",
    "Coffee": "Café",
    "Books": "Livros",
    "hosting": "hospedagem",
    "Investment": "Investimento",
    
    # Anteriores (migrados para regex para segurança)
    "age": "idade",
    "Age": "Idade",
    "actor": "ator",
    "Actor": "Ator",
    "actors": "atores",
    "Actors": "Atores",
    "people": "pessoas",
    "People": "Pessoas",
    "person": "pessoa",
    "Person": "Pessoa",
    "categories": "categorias",
    "Birthday": "Aniversário",
    "birthday": "aniversário",
    "Start": "Início",
    "End": "Fim",
    "Location": "Localização",
    "Runtime": "Duração",
    "Added": "Adicionado",
    "Soundtrack": "Trilha Sonora",
    "Theater": "Cinema",
    "Games": "Jogos",
    "Maker": "Criador",
    "Album": "Álbum",
    "Entry": "Entrada",
    "Recipes": "Receitas",
    "Ingredients": "Ingredientes",
    "Cuisine": "Culinária",
    "Events": "Eventos",
    "Projects": "Projetos",
    "All": "Todos",
    "Companies": "Empresas",
    "Meetings": "Reuniões",
    "Places": "Lugares",
    "Podcasts": "Podcasts",
    "Clippings": "Recortes",
    "Related": "Relacionados",
    "Metatype": "Metatipo",
    "Evergreen": "Perenes",
    "Travel": "Viagens",
    "Episodes": "Episódios",
    "Show": "Programa",
    "Guests": "Convidados",
    "Published": "Publicado",
    "Status": "Status",
    "Title": "Título",
    "Date": "Data",
    "Time": "Hora",
    "Type": "Tipo",
    "Tags": "Tags",
    "Link": "Link",
    "URL": "URL",
    "Owned": "Possuído",
    "Acquired": "Adquirido",
    "Price": "Preço",
    "Rating": "Avaliação",
    "Platform": "Plataforma",
    "Creator": "Criador",
    "Author": "Autor",
    "Genre": "Gênero",
    "Director": "Diretor",
    "Cast": "Elenco",
    "Plot": "Enredo",
    "Year": "Ano",
    "Name": "Nome",
}

# ==========================================
# 3. SUBSTITUIÇÕES LITERAIS (PHRASES/SYMBOLS)
# Use para frases ou termos com símbolos onde \b pode falhar ou não ser necessário
# ==========================================
subst_literais = {
    "Conference Sessons": "Sessões de Conferência", # Conforme solicitado (mesmo com typo original)
    "Conference Sessions": "Sessões de Conferência", # Correção preventiva
    "Job Interviews": "Entrevistas de Emprego",
    "Questions and topics": "Perguntas e tópicos",
    "music/genres": "música/gêneros",
    "To-watch": "Para assistir",
    "Favorites": "Favoritos",
    "Last seen": "Visto recentemente",
    "Last played": "Última vez jogado",
    "Board Games": "Jogos de Tabuleiro",
    "Cost per use": "Custo por uso",
    "Total uses": "Usos totais",
    "Per use": "Por uso",
    "Monthly uses": "Usos mensais",
}

def substituir_palavras():
    root_dir = "."
    extensions = (".md", ".base")
    count_files = 0
    
    print("Iniciando substituição de palavras com proteção de regex...")
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if ".obsidian" in dirpath:
            continue
            
        for filename in filenames:
            if not filename.endswith(extensions):
                continue
                
            filepath = os.path.join(dirpath, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Aplicar correções (Literais primeiro para consertar estragos)
                for old, new in correcoes.items():
                    if old in content:
                         content = content.replace(old, new)

                # 2. Aplicar substituições regex (palavras inteiras)
                for old, new in subst_palavras.items():
                    # \bword\b garante que só substitui a palavra inteira
                    pattern = r'\b' + re.escape(old) + r'\b'
                    content = re.sub(pattern, new, content)
                    
                # 3. Aplicar substituições literais
                for old, new in subst_literais.items():
                    if old in content:
                        content = content.replace(old, new)
                
                if content != original_content:
                    print(f"Alterado: {filepath}")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count_files += 1
                    
            except Exception as e:
                print(f"Erro ao processar {filepath}: {e}")

    print("-" * 30)
    print(f"Concluído! {count_files} arquivos foram modificados.")

if __name__ == "__main__":
    substituir_palavras()
