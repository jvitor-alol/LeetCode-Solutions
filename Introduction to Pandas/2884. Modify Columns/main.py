import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees


def main():
    data = {
        'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
        'salary': [19666, 74754, 62509, 54866]
    }
    df = pd.DataFrame(data)
    print(modifySalaryColumn(df))


if __name__ == "__main__":
    main()
