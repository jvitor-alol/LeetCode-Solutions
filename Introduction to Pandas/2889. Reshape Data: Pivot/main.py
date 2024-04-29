import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot(
        data=weather, index='month', columns='city', values='temperature')


def main():
    data = {
        'city': ['Jacksonville']*5 + ['ElPaso']*5,
        'month': ['January', 'February', 'March', 'April', 'May']*2,
        'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
    }
    df = pd.DataFrame(data)
    print(pivotTable(df))


if __name__ == "__main__":
    main()
