import os
import json

json_gold_prices = os.path.abspath("temp/gold_prices.json")
json_silver_prices = os.path.abspath("temp/silver_prices.json")


def gold_prices(gold_price):
    if os.path.exists(json_gold_prices):
        os.remove(json_gold_prices)

    KARAT = [
        "24K",
        "23K",
        "22K",
        "21K",
        "20K",
        "19K",
        "18K",
        "17K",
        "16K",
        "15K",
        "14K",
        "13K",
        "12K",
        "11K",
        "10K",
        "9K",
        "8K",
        "7K",
        "6K",
    ]

    PERCENTAGE = [
        99.990,
        95.824,
        91.658,
        87.491,
        83.325,
        79.159,
        74.993,
        70.826,
        66.660,
        62.494,
        58.328,
        54.161,
        49.995,
        45.829,
        41.663,
        37.496,
        33.330,
        29.164,
        24.998,
    ]

    prices = [round(per * gold_price / 100, 2) for per in PERCENTAGE]

    price_dict = [
        {"Karat": KARAT[i], "Percentage": PERCENTAGE[i], "Price": prices[i]}
        for i in range(len(prices))
    ]

    with open(json_gold_prices, "w") as gold_prices_file:
        json.dump(price_dict, gold_prices_file)


def silver_prices(silver_price):
    if os.path.exists(json_silver_prices):
        os.remove(json_silver_prices)

    KARAT = ["Ley 999", "Ley 950", "Ley 925", "Ley 800"]

    PERCENTAGE = [99.99, 95.00, 92.50, 80.00]

    prices = [round(per * silver_price / 100, 2) for per in PERCENTAGE]

    price_dict = [
        {"Karat": KARAT[i], "Percentage": PERCENTAGE[i], "Price": prices[i]}
        for i in range(len(prices))
    ]

    with open(json_silver_prices, "w") as silver_prices_file:
        json.dump(price_dict, silver_prices_file)
