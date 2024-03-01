import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    print(df)
    return df

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, students.columns[1:]]

def main():
    dados = {
        'student_id': [101, 53, 128, 3],
        'name': ['Ulysses', 'William', 'Henry', 'Henry'],
        'age': [13, 10, 6, 11]
    }
    student_data = pd.DataFrame(dados)
    print(selectData(student_data))
    
if __name__=="__main__":
    main()