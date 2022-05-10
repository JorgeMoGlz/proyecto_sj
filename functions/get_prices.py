import requests
from bs4 import BeautifulSoup


def gold_price():
    # URL del precio del oro en gramos
    KITCO_URL_GOLD = "https://www.kitco.com/gold-price-today-mexico/"

    # Obtenemos el request de la URL
    response = requests.get(KITCO_URL_GOLD)

    # Formato BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    gold_table = soup.find("div", class_="table-price--body-table--overview-detail")
    gram_row = gold_table.find_all("tr")[2]
    unformatted_gold_price = gram_row.find_all("td")[1].text
    gold_price = unformatted_gold_price.replace(",", "")

    return float(gold_price)


def silver_price():
    # URL del precio del oro en gramos
    KITCO_URL_SILVER = "https://www.kitco.com/silver-price-today-mexico/"

    # Obtenemos el request de la URL
    response = requests.get(KITCO_URL_SILVER)

    # Formato BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    silver_table = soup.find("div", class_="table-price--body-table--overview-detail")
    gram_row = silver_table.find_all("tr")[2]
    unformatted_silver_price = gram_row.find_all("td")[1].text
    silver_price = unformatted_silver_price.replace(",", "")

    return float(silver_price)
