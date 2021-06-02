import pandas as pd

def save(name, brand, description, notes, image_URL):
    idx = len(pd.read_csv("mylist.csv"))
    new_df = pd.DataFrame({"name":name,
                           "brand":brand,
                           "description":description,
                           "notes":notes,
                           "image_URL":image_URL},
                           index = [idx])

    new_df.to_csv("mylist.csv", mode = 'a', header=False)
    return None

def load_list():
    my_list = []
    df = pd.read_csv("mylist.csv")

    for i in range (len(df)):
        my_list.append(df.iloc[i].tolist())
    return my_list

def delete_all():
    idx = len(pd.read_csv("mylist.csv"))
    new_df = pd.DataFrame(index = [idx], columns=["name","brand","description","notes","image_URL"])

    new_df.to_csv("mylist.csv", header=False)
    return None