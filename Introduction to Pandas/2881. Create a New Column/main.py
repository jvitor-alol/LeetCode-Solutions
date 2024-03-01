import pandas as pd
from typing import List
    
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

def main():
    dados = {
        'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
        'salary': [4548, 28150, 1103, 6593, 74576, 24433]
    }
    df = pd.DataFrame(dados)
    print(createBonusColumn(df))
    
if __name__=="__main__":
    main()