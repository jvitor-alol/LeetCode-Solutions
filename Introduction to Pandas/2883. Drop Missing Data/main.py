import pandas as pd
from typing import List
    
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=['name'])
    return students

def main():
    data = {
        'student_id': [32, 217, 779, 849],
        'name': ['Piper', None, 'Georgia', 'Willow'],
        'age': [5, 19, 20, 14]
    }
    df = pd.DataFrame(data)
    print(dropMissingData(df))
    
if __name__=="__main__":
    main()