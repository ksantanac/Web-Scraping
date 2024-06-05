import time
import requests
import re
import pandas as pd
import math
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Define the URL to scrape
url = "https://www.gov.br/centraldebalancos/#/demonstracao-publicada/7646"

# Define headers to mimic a real browser
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition std-1)"}

# Set up Chrome options for headless browsing
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Open the main URL
driver.get(url)

# Allow time for the page to load
time.sleep(2)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find and extract the total number of items
qtd_itens = soup.find('div', id='listingCount').get_text().strip()

# Extract the number of items as an integer
index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

# Calculate the total number of pages
ultima_pagina = math.ceil(int(qtd) / 20)

# Dictionary to store product data
dic_produtos = {'marca' : [], 'preco' : []}

# Loop through all pages
for i in range(1, ultima_pagina + 1):
    # Construct the URL for the current page
    url_pag = f'{url}?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    driver.get(url_pag)

    # Allow time for the page to load
    time.sleep(2)

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all product elements
    produtos = soup.find_all('article', class_=re.compile('productCard'))

    # Loop through each product and extract details
    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()

        # Print the extracted product details (for debugging)
        print(marca, preco)

        # Append the product details to the dictionary
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

    # Print the current page URL (for debugging)
    print(url_pag)

# Close the browser
driver.quit()

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(dic_produtos)

# Save the DataFrame to a CSV file
df.to_csv('kabum.csv', encoding='utf-8', sep=';')
