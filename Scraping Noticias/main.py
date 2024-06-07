import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get("https://g1.globo.com")

content = response.content

site = BeautifulSoup(content, 'html.parser')

# Formato Html organizado
# print(site.prettify())

# HTML da notícia
noticias = site.findAll('div', attrs={'class' : 'feed-post-body'})

for noticia in noticias:

    # Título da noticia
    titulo = noticia.find('a', attrs={'class' : 'feed-post-link gui-color-primary gui-color-hover'})
    # print('Titulo da Noticia:')
    # print(titulo.text)
    #
    # print()
    # print('Link da Noticia')
    # print(titulo['href'])
    # print()

    # Subtitulo de texto
    subtitulo_text = noticia.find('div', attrs={'class' : 'feed-post-body-resumo'})

    # Subtitulo de ul
    subtitulo_ul = noticia.find('ul', attrs={'class': 'bstn-relateditems'})

    if (subtitulo_text):
        # print('Subtitulo da Noticia:')
        # print(subtitulo_text)
        # print()
        lista_noticias.append([titulo.text, subtitulo_text.text, titulo['href']])

    elif (subtitulo_ul):
        # print('Subtitulo da Noticia:')
        # print(subtitulo_ul.text)
        # print()
        lista_noticias.append([titulo.text, subtitulo_ul.text, titulo['href']])

    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])

print(news)