import os
import logging
from datetime import datetime

import sqlite3
from sqlite3 import Error
from turtle import up, update
from venv import create

logging.basicConfig(
    filename=os.path.abspath("database/db_logs.log"),
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

db_file = os.path.abspath("database/project_sj.db")

TABLES = [
    """CREATE TABLE gold_price(
        id_gold INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        actualization DATETIME NOT NULL,
        price REAL NOT NULL
    )
    """,
    """CREATE TABLE silver_price(
        id_silver INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        actualization DATETIME NOT NULL,
        price REAL NOT NULL
    )
    """,
    """CREATE TABLE purchase(
        id_purchase INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        purchase_date DATE NOT NULL,
        real_price REAL NOT NULL,
        purchase_price REAL NOT NULL,
        id_gold INTEGER NOT NULL REFERENCES gold_price(id_gold) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
        id_silver INTEGER NOT NULL REFERENCES silver_price(id_silver) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED
    )
    """,
    """CREATE TABLE piece(
        id_piece INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(150) NOT NULL,
        weight REAL NOT NULL,
        alloy VARCHAR(150) NOT NULL,
        id_purchase INTEGER NOT NULL REFERENCES purchase(id_purchase) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
        individual_real_price REAL NOT NULL,
        individual_purchase_price REAL NOT NULL
    )
    """,
]

# Creación de la conexión con la base de datos
def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        logging.critical("Error {} al establecer conexión con la base de datos".format(e))


# Creación de cada tabla en la base de datos
def create_table(conn, table):
    try:
        connection = conn.cursor()
        connection.execute(table)
    except Error as e:
        logging.critical("Error {} al crear tabla en la base de datos".format(e))


# Creación de la base de datos
def create_db(TABLES):
    for table in TABLES:
        create_table(create_connection(db_file), table)


# Checa si la base de datos ya existe
def database_exists():
    if not os.path.exists(db_file):
        create_db(TABLES)
        logging.info("Base de datos creada")

def gold_price_actualization(price):
    conn = create_connection(db_file)

    db = conn.cursor()

    actualization = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    update = (actualization, price)

    db.execute(
        """
            INSERT INTO gold_price(
                actualization, price
            )
            VALUES (?, ?)
        """, update
    )

    conn.commit()
    logging.info("Precio del oro actualizado")

def silver_price_actualization(price):
    conn = create_connection(db_file)

    db = conn.cursor()

    actualization = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    update = (actualization, price)

    db.execute(
        """
            INSERT INTO silver_price(
                actualization, price
            )
            VALUES (?, ?)            
        """, update
    )

    conn.commit()
    logging.info("Precio de la plata actualizado")


def query_gold_price():
    conn = create_connection(db_file)

    db = conn.cursor()

    db.execute(
        """
            SELECT *
            FROM gold_price
            ORDER BY id_gold
            DESC LIMIT 1;
        """
    )

    _,_,last_price = db.fetchall()[0]

    return last_price

def query_silver_price():
    conn = create_connection(db_file)

    db = conn.cursor()

    db.execute(
        """
            SELECT *
            FROM silver_price
            ORDER BY id_silver
            DESC LIMIT 1;
        """
    )

    _,_,last_price = db.fetchall()[0]

    return last_price