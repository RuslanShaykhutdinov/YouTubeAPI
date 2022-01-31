import numpy
import pandas as pd
import pylab
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

mpl.rcParams.update(mpl.rcParamsDefault)

df = pd.read_csv('youtube_vids.csv')
print(df.info())
print(df.isnull().sum())

sns.countplot(x='like_count', data=df.sample(5), palette='colorblind')
sns.set_style('darkgrid')
plt.title('5 Random Videos with Likes')
plt.xlabel('Count')
plt.ylabel('video_title')
plt.show()

sns.scatterplot(x='view_count', y='like_count', data=df, edgecolor='black', palette='cubehelix')
sns.set_style('darkgrid')
plt.title('Dependence between likes and views', size=16)
plt.xlabel('Views', size=12)
plt.ylabel('Likes', size=12)
plt.show()

z = numpy.polyfit(df['view_count'], df['like_count'], 1)
p = numpy.poly1d(z)
pylab.plot(df['view_count'], p(df['view_count']), "r--")
plt.show()

corr, _ = pearsonr(df['view_count'], df['like_count'])
print('Pearsons correlation: %.3f' % corr)
