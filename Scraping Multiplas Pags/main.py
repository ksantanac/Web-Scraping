import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k=samasung&__mk_pt_BR=ÅMÅŽÕÑ&crid=IKAVP8DAAOWT&sprefix=samasun%2Caps%2C223&ref=nb_sb_noss_2'

# Define headers to mimic a real browser
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition std-1)"}

def proxima_pagina(soup):
    # procurar botão próxima
    paginas = soup.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})

    # Ir na ultima pag com o botao prox desativado
    if not paginas.find('span', {'class' : 's-pagination-item s-pagination-next s-pagination-disabled'}):
        url = 'https://www.amazon.com.br/'
        prox = soup.find('a', 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator', href=True)
        url_final = (url + str(prox['href']))

        return url_final
    else:
        return

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

url = proxima_pagina(soup)
