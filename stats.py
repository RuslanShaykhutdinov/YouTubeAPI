import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams.update(mpl.rcParamsDefault)


def load_dataset(file_name):
    df1 = pd.read_csv(file_name)
    return df1


df = load_dataset('youtube_vids.csv')
print(df.info())
print(df.isnull().sum())
plt.title('5 Random Videos with Likes')
sns.set_style('darkgrid')
sns.countplot(x='like_count', data=df.sample(5), palette='colorblind')
plt.xlabel('Count')
plt.ylabel('video_title')
plt.show()

sns.set_style('darkgrid')
plt.title('Dependence between likes and views', size=16)
plt.xlabel('Views', size=12)
plt.ylabel('Likes', size=12)
sns.scatterplot(x='view_count', y='like_count', data=df, edgecolor='black', palette='cubehelix')
plt.show()

