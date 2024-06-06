import requests
from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com")

content = response.content

site = BeautifulSoup(content, 'html.parser')

# Formato Html organizado
# print(site.prettify())

# HTML da notícia
noticia = site.find('div', attrs={'class' : 'feed-post-body'})

# Título da noticia
titulo = noticia.find('a', attrs={'class' : 'feed-post-link gui-color-primary gui-color-hover'})
# print(titulo.text)

# Subtitulo
subtitulo = site.find('div', attrs={'class' : 'feed-post-body-resumo'})
print(subtitulo.text)