import requests
from bs4 import BeautifulSoup


def gold_price():
    """ Gold Price Function

    Función encargada de obtener el precio del oro por gramo de la página
    de kitco

    """
    # URL del precio del oro en gramos
    KITCO_URL_GOLD = "https://www.kitco.com/gold-price-today-mexico/"

    # Obtenemos el request de la URL
    response = requests.get(KITCO_URL_GOLD)

    # Formato BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Tabla donde se encuentran todos los precios en diferentes pesos
    gold_table = soup.find("div", class_="table-price--body-table--overview-detail")

    # Busqueda de la fila donde se encuentra el precio en gramos
    gram_row = gold_table.find_all("tr")[2]

    # Precio en gramos con coma
    unformatted_gold_price = gram_row.find_all("td")[1].text

    # Precio formateado sin coma
    gold_price = unformatted_gold_price.replace(",", "")

    # Retorna el precio en float
    return float(gold_price)


def silver_price():
    """ Silver Price Function

    Función encargada de obtener el precio de la plata por gramo de la página
    de kitco

    """
    # URL del precio del oro en gramos
    KITCO_URL_SILVER = "https://www.kitco.com/silver-price-today-mexico/"

    # Obtenemos el request de la URL
    response = requests.get(KITCO_URL_SILVER)

    # Formato BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Tabla donde se encuentran todos los precios en diferentes pesos
    silver_table = soup.find("div", class_="table-price--body-table--overview-detail")

    # Busqueda de la fila donde se encuentra el precio en gramos
    gram_row = silver_table.find_all("tr")[2]

    # Precio en gramos con coma
    unformatted_silver_price = gram_row.find_all("td")[1].text

    # Precio formateado sin coma
    silver_price = unformatted_silver_price.replace(",", "")

    # Retorna el precio en float
    return float(silver_price)
