"""General tools to extract text from Brazilian Chamber of Deputies."""


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the base URL for the website
base_url = "https://www.camara.leg.br/internet/sitaqweb/resultadoPesquisaDiscursos.asp?txOrador=&txPartido=&txUF=&dtInicio=01%2F11%2F2010&dtFim=03%2F11%2F2010&txTexto=&txSumario=&basePesq=plenario&CampoOrdenacao=dtSessao&PageSize=50&TipoOrdenacao=DESC&btnPesq=Pesquisar"

# Start a web browser and navigate to the page
driver = webdriver.Firefox()
driver.get(base_url)

# Find all the links to the texts on the page

links = driver.find_elements(By.CSS_SELECTOR, "a[href*='Sessao']")

links[0].click()
# /html/body/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[7]/td[4]/a
# /html/body/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[9]/td[4]/a
# /html/body/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[11]/td[4]/a
text_list = []
for link in links:
    # Click the link to navigate to the text page
    link.click()

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Retrieve the HTML content of the text page
    html = driver.page_source

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # Find the element containing the text
    text_element = soup.find("div", class_="text")

    # Get the text from the element
    text = text_element.text

    # Print the text
    text_list.append(text)

    # Navigate back to the previous page
    driver.back()

# Close the web browser
driver.close()
