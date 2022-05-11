import os
import logging
import sqlite3
from sqlite3 import Error

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
        print(e)


# Creación de cada tabla en la base de datos
def create_table(conn, table):
    try:
        connection = conn.cursor()
        connection.execute(table)
    except Error as e:
        print(e)


# Creación de la base de datos
def create_db(TABLES):
    for table in TABLES:
        create_table(create_connection(db_file), table)


# Checa si la base de datos ya existe
def database_exists():
    if not os.path.exists(db_file):
        create_db(TABLES)
        logging.info("Base de datos creada")
