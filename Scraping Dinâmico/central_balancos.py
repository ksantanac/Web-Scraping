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

produto = soup.find('div', class_='ui-card-body').get_text()

print((produto))
