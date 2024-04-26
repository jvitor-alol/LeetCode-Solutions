import pandas as pd
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    print(df)
    return df


def main():
    createDataframe([[1, 15], [2, 11], [3, 11], [4, 20]])


if __name__ == "__main__":
    main()
