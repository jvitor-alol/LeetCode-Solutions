import pandas as pd
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    print(df)
    return df


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)


def main():
    student_data = createDataframe([[1, 15], [2, 11], [3, 11], [4, 20]])
    print(getDataframeSize(student_data))


if __name__ == "__main__":
    main()
