import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

navegador.get('https://www.airbnb.com.br')

wait = WebDriverWait(navegador, 10)

sleep(2)

navegador.find_element(By.XPATH, '//*[@id="react-application"]/div/div/div[1]/div/div[6]/section/div[2]/div[2]/button').click()

try:
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-application"]/div/div/div[1]/div/div[6]/section/div[2]/div[2]/button')))
    element.click()
except Exception as e:
    print(f"Error: {e}")

# sleep(2)
# navegador.find_element(By.XPATH, '/html/body/div[11]/div/div/section/div/div/div[2]/div/div[1]/button/span/svg/path').click()





# inplut_place.send_keys('São Paulo')
# inplut_place.submit()


# site = BeautifulSoup(navegador.page_source, 'html.parser')

# print(site.prettify())





# navegador.quit()

