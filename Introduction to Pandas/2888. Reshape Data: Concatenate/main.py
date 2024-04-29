import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat((df1, df2), ignore_index=True)


def main():
    data_1 = {
        'student_id': [1, 2, 3, 4],
        'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
        'age': [8, 6, 15, 17]
    }
    data_2 = {
        'student_id': [5, 6],
        'name': ['Leo', 'Alex'],
        'age': [7, 7]
    }
    df1 = pd.DataFrame(data_1)
    df2 = pd.DataFrame(data_2)
    print(concatenateTables(df1, df2))


if __name__ == "__main__":
    main()
