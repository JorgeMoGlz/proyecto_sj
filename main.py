from operator import ge
import os
import sys

from models.ui_main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from functions import db, get_prices

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        db.database_exists()

        gold, silver = (get_prices.gold_price(), get_prices.silver_price())
        
        db.gold_price_actualization(gold)
        db.silver_price_actualization(silver)

        gold_price = db.query_gold_price()
        silver_price = db.query_silver_price()

        self.label_date.setText("Última actualización de precios: ")
        self.label_gold_price.setText("{}".format(gold_price))
        self.label.setText("{}".format(silver_price))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
