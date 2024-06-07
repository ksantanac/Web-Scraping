import requests
from bs4 import BeautifulSoup

# produto = input('Qual produto vc deja?')
produto_nome = 'Mi band 5'

url = f'https://lista.mercadolivre.com.br/{produto_nome}'

response = requests.get(url)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class' : 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:

    titulo = produto.find('h2', attrs={'class' : 'ui-search-item__title'})

    link = produto.find('a', attrs={'class' : 'ui-search-link'})

    real = produto.find('span', attrs={'class' : 'andes-money-amount__fraction'})
    
    centavos = produto.find('span', attrs={'class' : 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

    # print(produtos.prettify())
    print(f"Titulo do produto: {titulo.text}")
    print(f"Link do produto: {link['href']}")
    
    if (centavos):
        print(f"Preço: {real.text},{centavos.text}")
        
    else:
        print(f"Preço: {real.text},00")
    
    
    print('\n\n')
