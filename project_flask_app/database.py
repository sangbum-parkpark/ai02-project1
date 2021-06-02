import pandas as pd

def save(name, brand, description, notes):#, image_URL):
    idx = len(pd.read_csv("database.csv"))
    new_df = pd.DataFrame({"name":name,
                           "brand":brand,
                           "description":description,
                           "notes":notes},
                           index = [idx])

    new_df.to_csv("database.csv", mode = "a", header=False)
    return None

def load_list():
    perfume_list = []
    df = pd.read_csv("database.csv")
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis=1)
    if '' in df.columns:
        df = df.drop('', axis=1)

    for i in range (len(df)):
        perfume_list.append(df.iloc[i].tolist())
    return perfume_list
    # return perfume_list

def now_index():
    df = pd.read_csv("database.csv")
    return len(df)


def load_house(idx):
    df = pd.read_csv("database.csv")
    perfume_info = df.iloc[idx]
    return perfume_info


if __name__ == "__main__":
    load_list()
