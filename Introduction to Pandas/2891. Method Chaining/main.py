import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals[animals['weight'] > 100] \
        .sort_values(by='weight', ascending=False)[['name']]
    return df.reset_index(drop=True)


def main():
    data = {
        'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
        'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
        'age': [98, 50, 6, 45, 100, 26],
        'weight': [464, 41, 328, 463, 50, 349]
    }
    df = pd.DataFrame(data)
    print(findHeavyAnimals(df))


if __name__ == "__main__":
    main()
