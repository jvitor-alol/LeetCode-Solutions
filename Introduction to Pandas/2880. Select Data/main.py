import pandas as pd
from typing import List
    
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