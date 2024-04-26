import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.quantity = products.quantity.fillna(0)
    return products


def main():
    data = {
        'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
        'quantity': [None, None, 779, 849],
        'price': [135, 821, 9319, 3051]
    }
    df = pd.DataFrame(data)
    print(fillMissingValues(df))


if __name__ == "__main__":
    main()
