import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars='product', var_name='quarter', value_name='sales')


def main():
    data = {
        'product': ['Umbrella', 'SleepingBag'],
        'quarter_1': [417, 800],
        'quarter_2': [224, 936],
        'quarter_3': [379, 93],
        'quarter_4': [611, 875]
    }
    df = pd.DataFrame(data)
    print(meltTable(df))


if __name__ == "__main__":
    main()
