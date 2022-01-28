import pandas as pd


def load_dataset(file_name):
    df1 = pd.read_csv(file_name)
    return df1


df = load_dataset('youtube_vids.csv')
print(df)